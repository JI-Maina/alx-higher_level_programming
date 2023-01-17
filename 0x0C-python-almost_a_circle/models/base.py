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
                for instance in list_objs:
                    dict_str = [instance.to_dictionary()]
                    f.write(Base.to_json_string(dict_str))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): a string representing a list of dictionaries.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): key/word pair of attributes.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                r1 = cls(1, 1)
            else:
                r1 = cls(1)
            r1.update(**dictionary)
            return r1

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def __del__(self):
        pass
