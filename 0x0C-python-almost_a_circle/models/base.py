#!/usr/bin/python3
"""Defines a base class model."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): a list of instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
#     dict_str = [instance.to_dictionary() for instance in list_objs]
                for instance in list_objs:
                    dict_str = [instance.to_dictionary()]
                    f.write(Base.to_json_string(dict_str))
