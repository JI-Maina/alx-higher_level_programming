#!/usr/bin/python3
"""Defines a rectangle model class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): an integer.
            y (int): an integer.
            id (int): the id of the rectangle.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Returns the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Returns the rectangle's x value."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value of the rectangle."""
        self.__x = value

    @property
    def y(self):
        """Returns the rectangle's y value."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value of the rectangle."""
        self.__y = value
