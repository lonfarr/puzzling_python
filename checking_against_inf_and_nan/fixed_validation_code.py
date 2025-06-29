"""
This is the fixed code that can properly validate that infinity
and not a number inputs are not in an input sequence.

`python3 ./fixed_validation_code.py` will run unit tests.
"""

from collections.abc import Sequence
import math
import unittest


def fixed_sequence_values_are_finite(input_seq: Sequence[float]) -> bool:
    """
    Given an input sequence of floats checks that none of the values
    are infinity, negative infinity, or not a number (therefore finite).

    Returns True if all values are finite, otherwise False.
    """

    return all(map(math.isfinite, input_seq))


###########
# Testing #
###########
class TestFixedSequenceValuesAreFinite(unittest.TestCase):
    def test_empty_sequence(self) -> None:
        self.assertTrue(fixed_sequence_values_are_finite([]))

    def test_valid_sequence(self) -> None:
        self.assertTrue(
            fixed_sequence_values_are_finite([1.0, 0.0, -42.0, 47102378931.0])
        )

    def test_has_infinity(self) -> None:
        self.assertFalse(fixed_sequence_values_are_finite([1.0, math.inf, -2.0]))

    def test_has_negative_infinity(self) -> None:
        self.assertFalse(fixed_sequence_values_are_finite([1.0, -2.0, -math.inf]))

    def test_has_math_nan(self) -> None:
        self.assertFalse(fixed_sequence_values_are_finite([math.nan, 1.0, -2.0]))

    def test_has_float_nan(self) -> None:
        self.assertFalse(fixed_sequence_values_are_finite([float("nan"), 1.0, -2.0]))

    def test_has_float_infinity(self) -> None:
        self.assertFalse(fixed_sequence_values_are_finite([float("inf"), 1.0, -2.0]))

    def test_has_float_negative_infinity(self) -> None:
        self.assertFalse(fixed_sequence_values_are_finite([float("-inf"), 1.0, -2.0]))


if __name__ == "__main__":
    unittest.main()
