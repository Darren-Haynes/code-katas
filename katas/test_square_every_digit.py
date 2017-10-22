"""Test the ouput of square_digits function from square_every_digit module."""
import pytest

# test.assert_equals(square_digits(9119), 811181)

SQUARES = [
    (9119, 811181),
    (8765, 64493625),
    (8764, 64493616),
    (1234, 14916),
    (4321, 16941)
]


@pytest.mark.parametrize('nums_to_square, result', SQUARES)
def test_every_number_in_string_gets_squared(nums_to_square, result):
    """Test input string of digits return those digits squred"""
    from square_every_digit import square_digits
    assert square_digits(nums_to_square) == result
