"""
This is the code for the original function which contains an error
that passing in an iterable like a dictionary or a set will cause a TypeError.
"""

from collections.abc import Iterable
from dataclasses import dataclass
import unittest


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
class TestStoreRecordInDBIfNew(unittest.TestCase):
    def test_empty_list_adds_record(self) -> None:
        current_rows: list[DBRecord] = []
        row: DBRecord = DBRecord("Arthur Dent", 35)
        self.assertTrue(store_record_in_db_if_new(current_rows, row))

    def test_list_without_match_adds_record(self) -> None:
        current_rows: list[DBRecord] = [DBRecord("Ford Prefect", 200)]
        row: DBRecord = DBRecord("Arthur Dent", 35)
        self.assertTrue(store_record_in_db_if_new(current_rows, row))

    def test_list_with_match_does_not_add_record(self) -> None:
        current_rows: list[DBRecord] = [DBRecord("Arthur Dent", 35)]
        row: DBRecord = DBRecord("Arthur Dent", 35)
        self.assertFalse(store_record_in_db_if_new(current_rows, row))

    def test_empty_dict_adds_record(self):
        # NOTE: This test will fail, showing our error case
        current_rows: dict[DBRecord, str] = {}
        row: DBRecord = DBRecord("Arthur Dent", 35)
        self.assertTrue(store_record_in_db_if_new(current_rows, row))


if __name__ == "__main__":
    unittest.main()
