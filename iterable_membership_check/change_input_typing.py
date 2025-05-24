"""
This is the code for the "fixed" function that now will at least give
a static type error if a dictionary or set is passed in as an input.
"""

from collections.abc import Sequence
from dataclasses import dataclass
import unittest


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
class TestStoreRecordInDBIfNew(unittest.TestCase):
    def test_empty_list_adds_record(self) -> None:
        current_rows: list[DBRecord] = []
        row: DBRecord = DBRecord("Arthur Dent", 35)
        self.assertTrue(list_store_record_in_db_if_new(current_rows, row))

    def test_list_without_match_adds_record(self) -> None:
        current_rows: list[DBRecord] = [DBRecord("Ford Prefect", 200)]
        row: DBRecord = DBRecord("Arthur Dent", 35)
        self.assertTrue(list_store_record_in_db_if_new(current_rows, row))

    def test_list_with_match_does_not_add_record(self) -> None:
        current_rows: list[DBRecord] = [DBRecord("Arthur Dent", 35)]
        row: DBRecord = DBRecord("Arthur Dent", 35)
        self.assertFalse(list_store_record_in_db_if_new(current_rows, row))

    # This is an expected failure because we are explicitly ignoring the
    # type checker. This shows that this fix only shows type errors, it
    # can still fail at runtime.
    @unittest.expectedFailure
    def test_empty_dict_adds_record(self):
        # NOTE: This test will fail, showing our error case
        current_rows: dict[DBRecord, str] = {}
        row: DBRecord = DBRecord("Arthur Dent", 35)
        self.assertTrue(list_store_record_in_db_if_new(current_rows, row))  # type: ignore


if __name__ == "__main__":
    unittest.main()
