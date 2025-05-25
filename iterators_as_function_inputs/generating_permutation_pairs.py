"""
The `generate_pairs_from_iterable` generates permutations of the input.

This file shows that concrete iterables (like a list) work as intended,
but an iterator object will cause errors.
"""

from collections.abc import Iterable, Iterator
import unittest


def generate_pairs_from_iterable[T](input_iterable: Iterable[T]) -> list[tuple[T, T]]:
    """
    Given an input iterable, returns pairs of all possible permutations.

    For example, an input of [0, 1, 2] returns:
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    Note that ordering of the output is not guaranteed.
    """
    output_list: list[tuple[T, T]] = []
    for val_1 in input_iterable:
        for val_2 in input_iterable:
            output_list.append((val_1, val_2))
    return output_list


###########
# Testing #
###########
class TestGenerateParisFromIterable(unittest.TestCase):
    def test_empty_input(self) -> None:
        input_list: list[int] = []
        expected_output: list[tuple[int, int]] = []
        self.assertCountEqual(generate_pairs_from_iterable(input_list), expected_output)

    def test_single_item(self) -> None:
        input_list: list[int] = [0]
        expected_output: list[tuple[int, int]] = [(0, 0)]
        self.assertCountEqual(generate_pairs_from_iterable(input_list), expected_output)

    def test_two_items(self) -> None:
        input_list: list[int] = [0, 1]
        expected_output: list[tuple[int, int]] = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.assertCountEqual(generate_pairs_from_iterable(input_list), expected_output)

    def test_three_items(self) -> None:
        input_list: list[int] = [0, 1, 2]
        expected_output: list[tuple[int, int]] = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        ]
        self.assertCountEqual(generate_pairs_from_iterable(input_list), expected_output)

    def test_empty_iter(self) -> None:
        input_iter: Iterator[int] = iter([])
        expected_output: list[tuple[int, int]] = []
        self.assertCountEqual(generate_pairs_from_iterable(input_iter), expected_output)

    def test_single_item_iter(self) -> None:
        # NOTE: This will fail, showing an error case
        input_iter: Iterator[int] = iter([0])
        expected_output: list[tuple[int, int]] = [(0, 0)]
        self.assertCountEqual(generate_pairs_from_iterable(input_iter), expected_output)

    def test_two_item_iter(self) -> None:
        # NOTE: This will fail, showing an error case
        input_iter: Iterator[int] = iter([0, 1])
        expected_output: list[tuple[int, int]] = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.assertCountEqual(generate_pairs_from_iterable(input_iter), expected_output)

    def test_three_item_iter(self) -> None:
        # NOTE: This will fail, showing an error case
        input_iter: Iterator[int] = iter([0, 1, 2])
        expected_output: list[tuple[int, int]] = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (1, 1),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        ]
        self.assertCountEqual(generate_pairs_from_iterable(input_iter), expected_output)


if __name__ == "__main__":
    unittest.main()
