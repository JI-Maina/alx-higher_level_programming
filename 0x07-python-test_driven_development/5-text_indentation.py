#!/usr/bin/python3
""" Module that adds two new lines after characters: '.', ':', '?'"""


def text_indentation(text):
    """ Function that adds two lines after characters: '.', '?', ':'.

    Args:
        text (str): A string containing above characters

    Prints:
        same string as text but with two news lines after characters: '.', '?', ':'

    Raises:
        TypeError: text must be a string
    """
    if isinstance(text, str) == False:
        raise TypeError('text must be a string')

    list = ['.','?',':']

    for word in text:
        if word in list:
            print(word, end="")
            print()
            print()
        else:
            print(word, end="")
