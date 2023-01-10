#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a str at the end of a text file & returns no. of chars added.

    Aargs:
        filename: file to be append to.
        text (str): string to be appended.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
