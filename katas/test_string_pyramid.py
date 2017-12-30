"""Test string pyramid."""

import pytest

from string_pyramid import watch_pyramid_from_above
from string_pyramid import watch_pyramid_from_the_side
from string_pyramid import count_all_characters_of_the_pyramid
from string_pyramid import count_visible_characters_of_the_pyramid


def test_expected_side_view():
    """Test that side_view is correct."""
    expected = '  c  \n bbb \naaaaa'
    assert expected == watch_pyramid_from_the_side('abc')


def test_expected_top_view():
    """Test that top_view is correct."""
    expected = '''\
aaaaa
abbba
abcba
abbba
aaaaa'''
    assert expected == watch_pyramid_from_above('abc')


def test_visible_character_count():
    """Visible count should be 25 for input of 3 characters."""
    count = 25
    assert count_visible_characters_of_the_pyramid('abc') == count


def test_total_character_count():
    """Total character count should be 35 for input of 3 characters."""
    count = 35
    assert count_all_characters_of_the_pyramid('abc') == count