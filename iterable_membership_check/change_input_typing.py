"""
This is the code for the "fixed" function that now will at least give
a static type error if a dictionary or set is passed in as an input.
"""

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class DBRecord:
    name: str
    age: int


# Use a sequence as the type, which will likely eliminate any `__contains__` with hashing
def sequence_store_record_in_db_if_new(
    current_rows: Sequence[DBRecord], row: DBRecord
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


# Using a list for the input type will be explicit, but does limit "flexibility (eg: tuple for input)
def list_store_record_in_db_if_new(current_rows: list[DBRecord], row: DBRecord) -> bool:
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

    ###############################
    # Sequence input type testing #
    ###############################
    # All of the list test cases pass
    for test_case in test_cases:
        result: bool = sequence_store_record_in_db_if_new(
            test_case.input_current_rows, test_case.input_row
        )
        if result != test_case.expected_result:
            print(f"Test case ({test_case}) did not match expected result")
        else:
            print(f"Test case ({test_case}) passed!")

    # While the code still can be called with a dictionary, which will throw a type error at run time,
    # we now get a static type checking error. Thus, a robust testing framework would find this error.
    # I use `type: ignore` here so that I have a clean run of the type checker.
    try:
        result: bool = sequence_store_record_in_db_if_new({}, DBRecord("Arthur Dent", 35))  # type: ignore
        if result:
            print("Test case with empty dictionary passed")
        else:
            print("Test case with empty dictionary failed")
    except Exception as e:
        print(f"Exception {e} occurred when testing an empty dict as the iterable")

    ###########################
    # List input type testing #
    ###########################
    # All of the list test cases pass
    for test_case in test_cases:
        result: bool = list_store_record_in_db_if_new(
            test_case.input_current_rows, test_case.input_row
        )
        if result != test_case.expected_result:
            print(f"Test case ({test_case}) did not match expected result")
        else:
            print(f"Test case ({test_case}) passed!")

    # While the code still can be called with a dictionary, which will throw a type error at run time,
    # we now get a static type checking error. Thus, a robust testing framework would find this error.
    # I use `type: ignore` here so that I have a clean run of the type checker.
    try:
        result: bool = list_store_record_in_db_if_new({}, DBRecord("Arthur Dent", 35))  # type: ignore
        if result:
            print("Test case with empty dictionary passed")
        else:
            print("Test case with empty dictionary failed")
    except Exception as e:
        print(f"Exception {e} occurred when testing an empty dict as the iterable")


if __name__ == "__main__":
    main()
