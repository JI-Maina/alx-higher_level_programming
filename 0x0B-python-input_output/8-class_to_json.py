#!/usr/bin/python3
"""Defines a class_to_json module."""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure.

    Args:
        obj: class to be used.
    """
    return obj.__dict__
