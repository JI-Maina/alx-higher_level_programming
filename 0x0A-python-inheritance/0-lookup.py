#!/usr/bin/python3
"""A module that returns the list of available attr & methods of an obj """


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    """
    return dir(obj)
