"""Kata: Simple Pig Latin: - Move the first letter of each word to the end of
it, then add 'ay' to the end of the word.

#1 Best Practices Solution by dykchui & others

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
"""


def pig_it(text):
    """Change words from 'text' parameter string into pig latin words"""
    words = text.split()
    pyg_words = []
    for word in words:
        if not word.isalpha():
            pyg_words.append(word)
        else:
            pyg_words.append(word[1:] + word[0] + 'ay')

    return ' '.join(pyg_words)
