"""Test 'solution()' function from multiples_of_3_and_5 module"""
import pytest

NUMS_TABLE = [
    (10, 23),
    (9, 14),
    (8, 14),
    (7, 14),
    (6, 8),
]


@pytest.mark.parametrize('n, result', NUMS_TABLE)
def test_find_multiples_of_3_and_5_below_10(n, result):
    """test number sent into test_multiples function returns correct result"""
    from multiples_of_3_and_5 import solution
    assert solution(n) == result
