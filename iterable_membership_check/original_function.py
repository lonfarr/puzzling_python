"""
This is the code for the original function which contains an error
that passing in an iterable like a dictionary or a set will cause a TypeError.
"""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class DBRecord:
    name: str
    age: int


def store_record_in_db_if_new(current_rows: Iterable[DBRecord], row: DBRecord) -> bool:
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
    input_current_rows: list[DBRecord]
    input_row: DBRecord
    expected_result: bool


def main() -> None:
    # Test cases to run
    test_cases: list[TestCase] = [
        # 1) Empty list should add record
        TestCase([], DBRecord("Arthur Dent", 35), True),
        # 2) List without match should add record
        TestCase([DBRecord("Ford Prefect", 200)], DBRecord("Arthur Dent", 35), True),
        # 3) List with match should not add record
        TestCase([DBRecord("Arthur Dent", 35)], DBRecord("Arthur Dent", 35), False),
    ]

    # All of the list test cases pass
    for test_case in test_cases:
        result: bool = store_record_in_db_if_new(
            test_case.input_current_rows, test_case.input_row
        )
        if result != test_case.expected_result:
            print(f"Test case ({test_case}) did not match expected result")
        else:
            print(f"Test case ({test_case}) passed!")

    # This is a failure mode; an empty Dictionary throws a type error
    try:
        result: bool = store_record_in_db_if_new({}, DBRecord("Arthur Dent", 35))
        if result:
            print("Test case with empty dictionary passed")
        else:
            print("Test case with empty dictionary failed")
    except Exception as e:
        print(f"Exception {e} occurred when testing an empty dict as the iterable")


if __name__ == "__main__":
    main()
