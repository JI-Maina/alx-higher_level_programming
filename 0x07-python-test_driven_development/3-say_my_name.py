#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    if isinstance(first_name, str) == False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) == False:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
