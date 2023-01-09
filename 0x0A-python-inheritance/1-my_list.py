#!/usr/bin/python3
"""A class that inherits from list."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the sorted list in ascending sort."""
        print(sorted(self))
