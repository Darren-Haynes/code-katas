"""Kata: Sum of the first nth term of Series -  Your task is to write a
function which returns the sum of series upto nth term(parameter).

#1 Best Practices Solution by MMMAAANNN & others

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""

from __future__ import division


def series_sum(n):
    """Return sum of the first nth term of series"""
    if n == 0:
        return "0.00"

    num = 1.00
    while n > 1:
        divisor = n + n + (n-2)
        decimal = 1 / divisor
        num += decimal
        n -= 1
    return "{:.2f}".format(num)
