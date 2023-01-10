#!/usr/bin/python3
"""Reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Implementation of read_file.

    Args:
        filename (any): File to be read.
    """
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end='')
