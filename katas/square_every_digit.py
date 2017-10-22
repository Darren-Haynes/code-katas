"""Kata: Square Every Digits - square every digit of a number.

#1 Best Practices Solution by djm4686
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
"""

def square_digits(num):
    """Square every digit in the input string and return the square numbers"""
    return int(''.join([str(int(n) * int(n)) for n in str(num)]))
