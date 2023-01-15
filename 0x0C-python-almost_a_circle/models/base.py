#!/usr/bin/python3
"""Defines a base class model."""


class Base:
    """Base model.

    private class attribute:
        __nb_objects = 0 (int): number of instantiated bases.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base.

        Aargs:
            id (int): identity of the new base.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
