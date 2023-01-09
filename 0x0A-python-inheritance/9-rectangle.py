#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializes a new Rectangle.

        Args:
            width (int): width of new rectangle.
            height (int): height of new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns attributes of the rectangle."""
        string = '[' + str(self.__class__.__name__) + ']'
        string += f" {self.__width}/{self.__height}"
        return string
