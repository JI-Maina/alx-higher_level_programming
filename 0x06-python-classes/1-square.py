#!/usr/bin/python3

"""Defines a square by."""


class Square:
    """Represents a square."""
    def __init__(self, size=None):
        """Initializes a new square.

        args:
            size (int): The size of the new square.
        """

        self.__size = size
