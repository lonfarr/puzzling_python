"""
This is the code for the original function which contains an error
that passing in an iterable like a dictionary or a set will cause a TypeError.
"""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class FrozenDBRecord:
    name: str
    age: int


def store_record_in_db_if_new(
    current_rows: Iterable[FrozenDBRecord], row: FrozenDBRecord
) -> bool:
    """
    Given a list of the current rows, tests if the input row is already present.

    If row is already present, return False, indicated no changes to the DB.

    If row is not present, add to the database and return True.
    """
    if row in current_rows:
        return False

    # Value is not present in the current rows, so add to DB
    ############################################
    # This is where there would be a DB insert #
    ############################################
    return True


###########
# Testing #
###########
@dataclass
class TestCase:
    input_current_rows: list[FrozenDBRecord] | dict[FrozenDBRecord, str]
    input_row: FrozenDBRecord
    expected_result: bool


def main() -> None:
    # Test cases to run with both lists and dictionaries
    test_cases: list[TestCase] = [
        # 1) Empty list should add record
        TestCase([], FrozenDBRecord("Arthur Dent", 35), True),
        # 2) List without match should add record
        TestCase(
            [FrozenDBRecord("Ford Prefect", 200)],
            FrozenDBRecord("Arthur Dent", 35),
            True,
        ),
        # 3) List with match should not add record
        TestCase(
            [FrozenDBRecord("Arthur Dent", 35)],
            FrozenDBRecord("Arthur Dent", 35),
            False,
        ),
        # 4) Empty dictionary should add record
        TestCase({}, FrozenDBRecord("Arthur Dent", 35), True),
        # 5) Dictionary without a match should add record
        TestCase(
            {FrozenDBRecord("Ford Prefect", 200): "Alien"},
            FrozenDBRecord("Arthur Dent", 35),
            True,
        ),
        # 6) Dictionary with a match should not add record
        TestCase(
            {FrozenDBRecord("Arthur Dent", 35): "Human"},
            FrozenDBRecord("Arthur Dent", 35),
            False,
        ),
    ]

    # All of the test cases pass
    for test_case in test_cases:
        result: bool = store_record_in_db_if_new(
            test_case.input_current_rows, test_case.input_row
        )
        if result != test_case.expected_result:
            print(f"Test case ({test_case}) did not match expected result")
        else:
            print(f"Test case ({test_case}) passed!")


if __name__ == "__main__":
    main()
