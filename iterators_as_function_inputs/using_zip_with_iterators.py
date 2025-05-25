"""
This file showcases several issues with `zip` and passing in iterators.

If the iterator is utilized after calling `zip` but before all of the
values are evaluated by the generator, the output of `zip` will change.

If the first input is longer than the second input, it will iterate one past
the length of the second input. This can cause unexpected behavior if you are
assume zip only uses the number of items required.
"""

from collections.abc import Iterator


def main() -> None:
    # Iterator objects to get used for each of the examples
    iterator_1: Iterator[int]
    iterator_2: Iterator[int]
    zip_result: zip[tuple[int, int]]
    list_result: list[tuple[int, int]]

    # `zip` creates a generator, and it does not actually iterate over
    # the objects until it is accessed.
    # First, create a zip and print the results
    iterator_1 = iter([1, 2, 3, 4])
    iterator_2 = iter([-1, -2, -3, -4])
    zip_result = zip(iterator_1, iterator_2)
    list_result = list(zip_result)
    print(f"Zip result directly after doing the zip: {list_result}")

    # Do the same thing again, except call next on the first iterator after zip
    # is called before it is turned into a list, thus causing iterator_1 to
    # increment before it is accessed by the zip generator
    iterator_1 = iter([1, 2, 3, 4])
    iterator_2 = iter([-1, -2, -3, -4])
    zip_result: zip[tuple[int, int]] = zip(iterator_1, iterator_2)
    _ = next(iterator_1)
    list_result = list(zip_result)
    print(f"Zip result if next is called on an iterator first: {list_result}")

    # Another error case is that behavior of the iterator will depend on if the longer
    # iterator is passed in first or second.

    # Create longer and shorter iterators
    # And call zip with the longer iterator first
    iterator_1 = iter([1, 2, 3, 4])
    iterator_2 = iter([-1, -2])
    zip_result = zip(iterator_1, iterator_2)
    # Need to generate the list to run the zip generator
    _ = list(zip_result)
    print(f"When the longer iterator is passed first: {next(iterator_1)=}")

    # Recreate the longer and shorter iterator
    # This time call zip with the shorter iterator first
    iterator_1 = iter([1, 2, 3, 4])
    iterator_2 = iter([-1, -2])
    zip_result = zip(iterator_2, iterator_1)
    # Need to generate the list to run the zip generator
    _ = list(zip_result)
    print(f"When the longer iterator is passed second: {next(iterator_1)=}")


if __name__ == "__main__":
    main()
