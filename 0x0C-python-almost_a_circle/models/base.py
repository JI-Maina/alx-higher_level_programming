#!/usr/bin/python3
"""Defines a base class model."""
import json
import turtle
import csv


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

        content = []
        if list_objs is not None:
            for instance in list_objs:
                instance = instance.to_dictionary()
                json_dict = json.loads(cls.to_json_string(instance))
                content.append(json_dict)

        with open(filename, "w") as f:
            json.dump(content, f)

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

#   def __del__(self):
        pass

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV format representation of list_objs to a file.

        Args:
            list_objs (list): a list of instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='', encoding='utf8') as f:
            write_this = csv.writer(f, delimiter=' ')

            if cls.__name__ == "Rectangle":
                for instance in list_objs:
                    string = ""
                    instance = instance.to_dictionary()
                    string += (str(instance['id']) + ',' +
                            str(instance['width']) + ',' +
                            str(instance['height']) + ',' +
                            str(instance['x']) + ',' +
                            str(instance['y']))
                    write_this.writerow(string)

    
            if cls.__name__ == "Square":
                for instance in list_objs:
                    string = ""
                    instance = instance.to_dictionary()
                    string += (str(instance['id']) + ',' +
                            str(instance['width']) + ',' +
                            str(instance['height']) + ',' +
                            str(instance['x']) + ',' +
                            str(instance['y']))
                    write_this.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a csv of instances."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                        for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): A list of rectangle objects to draw.
            list_squares (list): A list of square objects to draw.
        """
        pic = turtle.Turtle()
        pic.screen.bgcolor("#b7312c")
        pic.pensize(3)
        pic.shape("turtle")

        pic.color("#ffffff")
        for rec in list_rectangles:
            pic.showturtle()
            pic.up()
            pic.goto(rec.x, rec.y)
            pic.down()

            for i in range(2):
                pic.forward(rec.width)
                pic.left(90)
                pic.forward(rec.width)
                pic.left(90)
            pic.hideturtle()

        pic.color("#b5e3d8")
        for sq in list_squares:
            pic.showturtle()
            pic.penup()
            pic.goto(sq.x, sq.y)
            pic.pendown()

            for i in range(4):
                pic.forward(sq.width)
                pic.left(90)
            pic.hideturtle()

        turtle.exitonclick()
