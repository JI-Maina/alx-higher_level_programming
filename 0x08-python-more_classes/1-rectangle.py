#!/usr/bin/python3
""" A module that defines a rectangle."""


class Rectangle:
    """Creates a rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes a rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width

        @property
        def width(self):
            """Returns the width of the rectangle.
            """
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle.
            
            Args:
                value (int): width of the rectangle.

            Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
            """
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

        @property
        def height(self):
            """Retrieves and returns height of rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height of the rectangle.

            Args:
                value (int): integer to set as height.

            Raises:
                TypeError: height must be an integer
                ValueError: height must be >= 0
            """
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
