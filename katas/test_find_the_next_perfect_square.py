"""Tests 'find_next_square()' function from fine_the_next_perfect_square.py"""
import pytest


NUMS_TABLE = [
    (121, 144),
    (625, 676),
    (319225, 320356),
    (15241383936, 15241630849),
    (155, -1),
    (15241383936, 15241630849),
    (1, 4),
    (9, 16),
    (16, 25),
    (25, 36)
]


@pytest.mark.parametrize('sq, result', NUMS_TABLE)
def test_next_perfect_square_is_achieved(sq, result):
    """Checks that items in first input list are not in second input list"""
    from find_the_next_perfect_square import find_next_square
    assert find_next_square(sq) == result
