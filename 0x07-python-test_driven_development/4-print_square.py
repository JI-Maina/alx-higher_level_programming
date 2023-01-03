#!/usr/bin/python3


def print_square(size):
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
