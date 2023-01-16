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

        Raises:
            TypeError: if width, height, x or y is not an integer.
            ValueError: if width or height is under or equals 0.
            ValueError: If x or y is under 0.

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
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Returns the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Returns the rectangle's x value."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value of the rectangle."""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Returns the rectangle's y value."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value of the rectangle."""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
#       [print("") for m in range(self.y)]
        for m in range(self.y):
            print("")
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end="")
            for k in range(self.width):
                print('#', end="")
            print()
#            [print('_', end='') for k in range(self.x)]
#            [print('#', end='') for j in range(self.width)]

    def __str__(self):
        """Returns string representation of rectangle instance."""
        return "[Rectangle]" + \
            f" ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.

        Args:
            args (tuple): new values.
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute

        kwargs:
            kwargs (dict): contains a key/word pair of new arguements.
        """
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.height = arg
                elif x == 3:
                    self.x = arg
                elif x == 4:
                    self.y = arg
                x += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
