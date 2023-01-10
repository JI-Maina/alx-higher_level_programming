#!/usr/bin/python3
"""Defines class MyInt."""


class MyInt(int):
    """Represents an int."""

    def __eq__(self, value):
        """Overwrites equal operator with not equal behavior.

        Args:
            value (int): An integer.

        Returns: Opposite of the == operator.
        """
        return self.real != value

    def __ne__(self, value):
        """Overwites not equal operator with equal behavior.

        Args:
            value (int): An integer.

        Returns: Opposite of the != operator.
        """
        return self.real == value
