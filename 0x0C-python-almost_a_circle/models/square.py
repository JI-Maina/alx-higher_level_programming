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

    def update(self, *args, **kwargs):
        """Updates square attributes.

        Args:
            args (tuple): different attributes grouped as a tuple.
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute

            kwargs (dict): key/word pair of attributes passed as a dict.
        """
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    self.id = arg
                elif x == 1:
                    self.width = arg
                    self.height = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.width = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
            }
