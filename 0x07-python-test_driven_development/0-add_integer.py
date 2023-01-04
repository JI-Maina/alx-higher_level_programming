#!/usr/bin/python3
""" Module to add two integers """



def add_integer(a, b=98):
    """ Function that adds two integers.

    Args:
        a (int)
        b (int)

    Return:
        sum of a and b

    Raise:
        TypeError if a and b are not integers
    """
    if isinstance(a, float) == True:
        a = int(a)
    elif isinstance(a, int) == False:
        raise TypeError('a must be an integer')

    if isinstance(b, float) == True:
        b = int(b)
    elif isinstance(b, int) == False:
        raise TypeError('b must be an integer')
    
    return a + b
