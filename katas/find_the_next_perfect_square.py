"""Kata: Find The Next Perfect Square - Complete the findNextSquare method
that finds the next integral perfect square after the one passed as a
parameter.


#1 Best Practices Solution by noreng & others

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
"""


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = sq ** 0.5
    if sq == int(root) * int(root):
        return (root + 1) * (root + 1)
    return -1
