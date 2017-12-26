"""Kata: String Pyramid -  You have to build a pyramid.

This pyramid should be built from characters from a given string.

#1 Best Practice Solution by Blind4Basics

def array_diff(a, b):
    return [x for x in a if x not in b]

def watch_pyramid_from_the_side(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( ' '*(i) + characters[i]*(baseLen-2*i) + ' '*(i) for i in range(len(characters)-1,-1,-1) )


def watch_pyramid_from_above(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( characters[0:min(i,baseLen-1-i)] + characters[min(i,baseLen-1-i)]*(baseLen-2*min(i,baseLen-1-i)) + characters[0:min(i,baseLen-1-i)][::-1] for i in range(baseLen) )


def count_visible_characters_of_the_pyramid(characters):
    return -1 if not characters else (len(characters)*2-1)**2


def count_all_characters_of_the_pyramid(characters):
    return -1 if not characters else sum( (2*i+1)**2 for i in range(len(characters)) )
"""


def watch_pyramid_from_the_side(characters):
    if not characters:
        return characters

    pyramid = []
    no_of_chars = len(characters) * 2 - 1
    for i, char in enumerate(characters):
        chars = [char] * no_of_chars
        if i == 0:
           pyramid.append(chars)
        else:
            spaces = [' '] * i
            pyramid.append(spaces + chars + spaces)

        no_of_chars -= 2

    pp = ""
    for row in reversed(pyramid):
        p_row = ''.join(row) + '\n'
        pp += p_row

    return pp.strip('\n')


def watch_pyramid_from_above(characters):
    if not characters:
        return characters

    char_len = len(characters)
    last_idx = char_len * 2 - 2
    center = char_len - 1
    pyramid = [[] for _ in range(char_len * 2 - 1)]

    for i, row in enumerate(pyramid):
        for j in range(char_len * 2 - 1):
            if i == 0 or j == 0 or i == last_idx or j == last_idx:
                row.append(characters[0])
            elif i == center and j == center:
                row.append(characters[center])
            else:
                char = max(abs(center - i), abs(center - j))
                row.append(characters[center - char])

    pp = ""
    for row in pyramid:
        p_row = ''.join(row) + '\n'
        pp += p_row

    return pp.strip()


def count_visible_characters_of_the_pyramid(characters):
    if not characters:
        return -1

    char_len = len(characters)
    width = char_len * 2 - 1
    return width * width


def count_all_characters_of_the_pyramid(characters):
    if not characters:
        return -1

    total = 0
    start = len(characters) * 2 - 1
    while start > 0:
        total += start * start
        start = start - 2
    return total
