#!/usr/bin/python3

"""Defines a square by."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        args:
            size (int): The size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of a square.

        args:
            value (int): The size of the new square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
