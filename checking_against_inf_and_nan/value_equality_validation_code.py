"""
This is the code that checks a sequence of floats to ensure all
are finite (no infinity or NaNs). Specifically this code does not
use the `in` operator, but manually compares with `==`.

`math.inf`, `float("inf")`, `-math.inf`, and `float("-inf")` are
all validated properly, but `math.nan` and `float("nan")` do not
validate properly due to how NaN is handled in comparisons.

Note that this is different than then original code where `math.nan`
worked properly.

`python3 ./value_equality_validation_code.py` will run unit tests.
"""

from collections.abc import Sequence
import math
import unittest


def value_equality_based_sequence_values_are_finite(
    input_seq: Sequence[float],
) -> bool:
    """
    Given an input sequence of floats checks that none of the values
    are infinity, negative infinity, or not a number (therefore finite).

    Returns True if all values are finite, otherwise False.
    """

    for val in input_seq:
        if val == math.inf or val == -math.inf or val == math.nan:
            return False
    return True


###########
# Testing #
###########
class TestEqualityBasedSequenceValuesAreFinite(unittest.TestCase):
    def test_empty_sequence(self) -> None:
        self.assertTrue(value_equality_based_sequence_values_are_finite([]))

    def test_valid_sequence(self) -> None:
        self.assertTrue(
            value_equality_based_sequence_values_are_finite(
                [1.0, 0.0, -42.0, 47102378931.0]
            )
        )

    def test_has_math_infinity(self) -> None:
        self.assertFalse(
            value_equality_based_sequence_values_are_finite([1.0, math.inf, -2.0])
        )

    def test_has_negative_math_infinity(self) -> None:
        self.assertFalse(
            value_equality_based_sequence_values_are_finite([1.0, -2.0, -math.inf])
        )

    def test_has_math_nan(self) -> None:
        self.assertFalse(
            value_equality_based_sequence_values_are_finite([math.nan, 1.0, -2.0])
        )

    def test_has_float_nan(self) -> None:
        # NOTE: This test will fail, showing our error case
        self.assertFalse(
            value_equality_based_sequence_values_are_finite([float("nan"), 1.0, -2.0])
        )

    def test_has_float_infinity(self) -> None:
        self.assertFalse(
            value_equality_based_sequence_values_are_finite([float("inf"), 1.0, -2.0])
        )

    def test_has_float_negative_infinity(self) -> None:
        self.assertFalse(
            value_equality_based_sequence_values_are_finite([float("-inf"), 1.0, -2.0])
        )


if __name__ == "__main__":
    unittest.main()
