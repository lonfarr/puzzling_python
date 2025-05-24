"""
Show how `in` and `not in` works with classes that define one
of the following (but not the others):
1) `__contains__`
2) `__iter__`
3) `__getitem__`

This is to prove the the information about membership test operations works
https://docs.python.org/3/reference/expressions.html#membership-test-operations
"""

from collections.abc import Iterator
import unittest


class SimpleList[T]:
    def __init__(self) -> None:
        self.internal_list: list[T] = []

    def append(self, val: T) -> None:
        self.internal_list.append(val)


class ContainsOnlyList[T](SimpleList[T]):
    def __contains__(self, item: T):
        return item in self.internal_list


class IterOnlyList[T](SimpleList[T]):
    def __iter__(self) -> Iterator[T]:
        return iter(self.internal_list)


class GetItemOnlyList[T](SimpleList[T]):
    def __getitem__(self, index: int) -> T:
        if index >= len(self.internal_list) or index < 0:
            raise IndexError
        return self.internal_list[index]


class TestContainsOnlyList(unittest.TestCase):
    def setUp(self) -> None:
        self.test_list: ContainsOnlyList[int] = ContainsOnlyList()

        self.item_in_list: int = 42
        self.test_list.append(self.item_in_list)

        self.item_not_in_list: int = -1

    def test_in_returns_false(self) -> None:
        self.assertFalse(self.item_not_in_list in self.test_list)

    def test_in_return_true(self) -> None:
        self.assertTrue(self.item_in_list in self.test_list)

    def test_not_in_returns_false(self) -> None:
        self.assertFalse(self.item_in_list not in self.test_list)

    def test_not_in_returns_true(self) -> None:
        self.assertTrue(self.item_not_in_list not in self.test_list)


class TestIterOnlyList(unittest.TestCase):
    def setUp(self) -> None:
        self.test_list: IterOnlyList[int] = IterOnlyList()

        self.item_in_list: int = 42
        self.test_list.append(self.item_in_list)

        self.item_not_in_list: int = -1

    def test_in_returns_false(self) -> None:
        self.assertFalse(self.item_not_in_list in self.test_list)

    def test_in_return_true(self) -> None:
        self.assertTrue(self.item_in_list in self.test_list)

    def test_not_in_returns_false(self) -> None:
        self.assertFalse(self.item_in_list not in self.test_list)

    def test_not_in_returns_true(self) -> None:
        self.assertTrue(self.item_not_in_list not in self.test_list)


class TestGetItemOnlyList(unittest.TestCase):
    def setUp(self) -> None:
        self.test_list: GetItemOnlyList[int] = GetItemOnlyList()

        self.item_in_list: int = 42
        self.test_list.append(self.item_in_list)

        self.item_not_in_list: int = -1

    def test_in_returns_false(self) -> None:
        self.assertFalse(self.item_not_in_list in self.test_list)

    def test_in_return_true(self) -> None:
        self.assertTrue(self.item_in_list in self.test_list)

    def test_not_in_returns_false(self) -> None:
        self.assertFalse(self.item_in_list not in self.test_list)

    def test_not_in_returns_true(self) -> None:
        self.assertTrue(self.item_not_in_list not in self.test_list)


if __name__ == "__main__":
    unittest.main()
