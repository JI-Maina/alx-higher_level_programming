#!/usr/bin/python3
"""Defines a square model."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square.

        args:
            size (int): the width and height of the square.
            x (int): x position of the square.
            y (int): y position of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of square istance."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the new square size.

        Args:
            value (int): new size of the square.

        """
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
