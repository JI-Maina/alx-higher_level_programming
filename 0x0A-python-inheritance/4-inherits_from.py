#!/usr/bin/python3
"""A module that checks subclass."""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.

    Args:
        obj: object to be checked if it belongs to a subclass.
        a_class: class to be checked against.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
