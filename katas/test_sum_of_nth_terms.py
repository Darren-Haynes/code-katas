"""Test the sum-of-nth-term-series function."""

import pytest

NUMS_TABLE = [
    (1, "1.00"),
    (2, "1.25"),
    (3, "1.39"),
    (0, "0.00"),
    (4, "1.49"),
    (5, "1.57"),
    (6, "1.63")
]


@pytest.mark.parametrize('n, result', NUMS_TABLE)
def test_that_the_right_string_represented_float_is_returned(n, result):
    """Test that input num returns the correct result"""
    from sum_of_nth_terms import series_sum
    assert series_sum(n) == result
