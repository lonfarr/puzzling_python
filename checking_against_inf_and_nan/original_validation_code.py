"""
This is the original code a function that checks a sequence
of floats to ensure all are finite (no infinity or NaNs).

`math.inf`, `float("inf")`, `-math.inf`, and `float("-inf")`, and
`math.nan` are all properly validated but `float("nan")` is not
due to an error in how NaN is compared.

`python3 ./original_validation_code.py` will run unit tests.
"""

from collections.abc import Sequence
import math
import unittest


def sequence_values_are_finite(input_seq: Sequence[float]) -> bool:
    """
    Given an input sequence of floats checks that none of the values
    are infinity, negative infinity, or not a number (therefore finite).

    Returns True if all values are finite, otherwise False.
    """

    for val in input_seq:
        if val in [math.inf, -math.inf, math.nan]:
            return False
    return True


###########
# Testing #
###########
class TestSequenceValuesAreFinite(unittest.TestCase):
    def test_empty_sequence(self) -> None:
        self.assertTrue(sequence_values_are_finite([]))

    def test_valid_sequence(self) -> None:
        self.assertTrue(sequence_values_are_finite([1.0, 0.0, -42.0, 47102378931.0]))

    def test_has_math_infinity(self) -> None:
        self.assertFalse(sequence_values_are_finite([1.0, math.inf, -2.0]))

    def test_has_negative_math_infinity(self) -> None:
        self.assertFalse(sequence_values_are_finite([1.0, -2.0, -math.inf]))

    def test_has_math_nan(self) -> None:
        self.assertFalse(sequence_values_are_finite([math.nan, 1.0, -2.0]))

    def test_has_float_nan(self) -> None:
        # NOTE: This test will fail, showing our error case
        self.assertFalse(sequence_values_are_finite([float("nan"), 1.0, -2.0]))

    def test_has_float_infinity(self) -> None:
        self.assertFalse(sequence_values_are_finite([float("inf"), 1.0, -2.0]))

    def test_has_float_negative_infinity(self) -> None:
        self.assertFalse(sequence_values_are_finite([float("-inf"), 1.0, -2.0]))


if __name__ == "__main__":
    unittest.main()
