#!/usr/bin/python3
"""Defines an empty class base geometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an Exception."""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name (str): A string.
            value (int): An integer ot be validated.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
