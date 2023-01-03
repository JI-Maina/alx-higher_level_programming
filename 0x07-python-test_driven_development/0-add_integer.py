#!/usr/bin/python3



def add_integer(a, b=98):
    if isinstance(a, float) == True:
        a = int(a)
    elif isinstance(a, int) == False:
        raise TypeError('a must be an integer')

    if isinstance(b, float) == True:
        b = int(b)
    elif isinstance(b, int) == False:
        raise TypeError('b must be an integer')
    
    return a + b
