"""Test forbes.py."""

import pytest
from forbes import billionaires

youngest, under80 = billionaires()


def test_dicts_returned():
    """Two dicts should be returned."""
    d1, d2 = billionaires()
    assert isinstance(d1, dict)
    assert isinstance(d2, dict)


def test_youngest_billionaires_name():
    """Youngest Billionaire should be Mark Zuckerberg."""
    name = 'Mark Zuckerberg'
    assert youngest['name'] == name


def test_under80_billionaires_name():
    """Oldest Billionaire under 80 should be Phil Knight."""
    name = 'Phil Knight'
    assert under80['name'] == name


def test_youngest_billionaires_age():
    """Youngest Billionaire's age should be 32."""
    age = 32
    assert youngest['age'] == age


def test_oldest_under80_billionaires_age():
    """Oldest Billionaire's age under 80 should be 78."""
    age = 78
    assert under80['age'] == age


def test_youngest_billionaires_net_worth():
    """Youngest Billionaire's net worth should be 4460000000."""
    net_worth = 44600000000
    assert youngest['net_worth (USD)'] == net_worth


def test_oldest_under80_billionaires_net_worth():
    """Oldest Billionaire's net worth under 80 should be 2440000000."""
    net_worth = 24400000000
    assert under80['net_worth (USD)'] == net_worth


def test_youngest_billionaires_source():
    """Youngest Billionaire's source should be Facebook."""
    source = 'Facebook'
    assert youngest['source'] == source


def test_oldest_under80_billionaires_source():
    """Oldest Billionaire's source should be Nike."""
    source = 'Nike'
    assert under80['source'] == source
