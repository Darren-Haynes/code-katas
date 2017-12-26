"""Kata: Array.diff -  implement an difference function, which subtracts one
list from another. A 6kyu kata.

#1 Best Practices Solution by jmc04 & others

def array_diff(a, b):
    return [x for x in a if x not in b]
"""


def array_diff(a, b):
    """Return list of numbers in parameter 'a' if not in parameter 'b'"""
    l = []
    for i in a:
    	if i not in b:
        	l.append(i)
    return l
