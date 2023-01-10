#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square."""

    def __init__(self, size):
        """Instantiates a Square.

        Args:
            size (int): length & width of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
