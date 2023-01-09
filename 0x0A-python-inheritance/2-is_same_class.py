#!/usr/bin/python3
"""A module that checks type."""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj: object to be checked.
        a_class: class to check if obj belongs to.
    """
    if type(obj) == a_class:
        return True
    return False
