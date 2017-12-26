"""Kata: Find The Odd Int - Given an array, find the int that appears an odd
number of times.

#1 Best Practices Solution by cerealdinner & others

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""


def find_it(seq):
    """Find the number that appears an odd number of times in the input list"""
    count = {}
    for n in seq:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    for k in count:
        if count[k] % 2 != 0:
            return k
