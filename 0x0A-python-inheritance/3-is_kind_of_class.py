#!/usr/bin/python3
"""A module that checks class."""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified class;
        otherwise False.

    Args:
        obj: object to check it's class.
        a_class: class to counter-check with.
    """
    if isinstance(obj, a_class):
        return True
    return False
