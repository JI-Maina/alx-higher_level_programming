#!/usr/bin/python3
""" A module that defines a rectangle."""


class Rectangle:
    """Creates a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    def area(self):
        """Returns the rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Print the rectangle with the character #."""
        if self.__width == 0 or self.height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message, when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.

        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rec_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
