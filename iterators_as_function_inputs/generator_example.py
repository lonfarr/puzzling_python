"""
This file shows a simple generator example and how the size
of a generator and its total result can be drastically different.

It also includes some unit testing to prove it is correct.
"""

from collections.abc import Generator
import sys
import unittest


def fib_generator(n: int) -> Generator[int]:
    """
    Returns a generator for the first n Fibonacci values
    """
    if n >= 1:
        # If there is at least one return, the first value is 0
        yield 0

        # All other values we must count
        count: int = 1
        # By doing this weird logic, we get "1" twice to start
        cur_val: int = 0
        prev_val: int = 1
        while n > count:
            prev_val, cur_val = cur_val, prev_val + cur_val
            yield cur_val
            count += 1


########
# Main #
########
def main() -> None:
    # Typing our reused variables
    fib_gen: Generator[int]
    fib_list: list[int]

    # Test with varying sizes of n to get size of the generator and the list
    for fib_n in [0, 10, 100, 1000]:
        fib_gen = fib_generator(fib_n)
        fib_list = list(fib_generator(fib_n))
        print(f"Size of generator for n={fib_n} is {sys.getsizeof(fib_gen)} bytes")
        print(f"Size of list for n={fib_n} is {sys.getsizeof(fib_list)} bytes")


###########
# Testing #
###########
class TestFibGenerator(unittest.TestCase):
    def test_fib_generator_n_less_than_zero(self) -> None:
        # When input is less than 0, generator should have no data
        output_list: list[int] = list(fib_generator(-1))
        self.assertCountEqual(output_list, [])

    def test_fib_generator_n_equals_zero(self) -> None:
        # When input is 0, generator should have no data
        output_list: list[int] = list(fib_generator(0))
        self.assertCountEqual(output_list, [])

    # Test several cases when n > 1
    def test_fib_generator_n_equals_one(self) -> None:
        output_list: list[int] = list(fib_generator(1))
        self.assertCountEqual(output_list, [0])

    def test_fib_generator_n_equals_two(self) -> None:
        output_list: list[int] = list(fib_generator(2))
        self.assertCountEqual(output_list, [0, 1])

    def test_fib_generator_n_equals_three(self) -> None:
        output_list: list[int] = list(fib_generator(3))
        self.assertCountEqual(output_list, [0, 1, 1])

    def test_fib_generator_n_equals_four(self) -> None:
        output_list: list[int] = list(fib_generator(4))
        self.assertCountEqual(output_list, [0, 1, 1, 2])

    def test_fib_generator_n_equals_ten(self) -> None:
        output_list: list[int] = list(fib_generator(10))
        self.assertCountEqual(output_list, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


if __name__ == "__main__":
    main()

    unittest.main()
