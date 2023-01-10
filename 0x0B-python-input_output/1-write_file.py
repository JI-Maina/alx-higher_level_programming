#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Writes a str to a text file and returns the number of chars written.

    Args:
        filename: file to be written into.
        text (str): string to be written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
