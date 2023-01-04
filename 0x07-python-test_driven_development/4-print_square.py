#!/usr/bin/python3
""" Module that prints a square with character #. """


def print_square(size):
    """ Function that prints a square with character '#'.

    Args:
        size (int): length of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if isinstance(size, float) == True:
        if size < 0:
            raise TypeError('size must be an integer')
        else:
            size = int(size)
    elif isinstance(size, int) == False:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print("#" * size)
