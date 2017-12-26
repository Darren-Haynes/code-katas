"""Test the 'find_it()' function in find_the_odd_int.py module"""
import pytest

SEQ_TABLE = [
    ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
    ([1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 6], 3),
    ([0, 1, 1, 10, 10, 20, 20], 0),
    ([-1, -2, -1, -3, -2, -4, -3], -4),
    ([1000, 2000, 3000, 4000, 1000, 3000, 4000], 2000)
]


@pytest.mark.parametrize('seq, result', SEQ_TABLE)
def test_that_odd_integer_is_found(seq, result):
    """test that odd integer is found"""
    from find_the_odd_int import find_it
    assert find_it(seq) == result
