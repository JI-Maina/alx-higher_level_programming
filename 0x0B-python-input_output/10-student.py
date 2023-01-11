#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student.

        Args:
            first_name (str): student's first name.
            last_name (str): student's last name.
            age (int): student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): optional list of attribute names.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
