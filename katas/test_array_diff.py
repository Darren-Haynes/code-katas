"""Tests for array_diff funtion in module array_diff"""
import pytest


LISTS_TABLE = [
    ([1, 2], [1], [2]),
    ([1, 2, 2], [1], [2, 2]),
    ([1, 2, 2], [2], [1]),
    ([1, 2, 2], [], [1, 2, 2]),
    ([], [1, 2], []),
    ([1, 2, 3, 4, 5], [6, 7], [1, 2, 3, 4, 5]),
    ([1, 1, 1, 1, 1], [1, 2], []),
    ([101, 202, 303], [101], [202, 303]),
    ([101, 202, 303], [101, 303], [202])
]


@pytest.mark.parametrize('a, b, result', LISTS_TABLE)
def test_items_in_one_list_are_not_in_another(a, b, result):
    """Checks that items in first input list are not in second input list"""
    from array_diff import array_diff
    assert array_diff(a, b) == result
