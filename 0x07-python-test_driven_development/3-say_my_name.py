#!/usr/bin/python3
""" Module that prints full name """


def say_my_name(first_name, last_name=""):
    """ Function that prints full name.

    Args:
        first_name (str): first name
        last_name (str): last name

    Prints:
        full name formated in str
        " My name is <first name> <last name>"

    Raises:
        TypeError: if first_name or last_name is not str
    """
    if isinstance(first_name, str) == False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) == False:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
