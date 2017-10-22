"""Kata: Multiple of 3 and 5 - list all the natural numbers below 10 that
are multiples of 3 or 5.

#1 Best Practices Solution by Process & others

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""


def solution(number):
    """get all multiples of 3 and 5 from list of digits if digit below 10"""
    multiples = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiples += i
    return multiples
