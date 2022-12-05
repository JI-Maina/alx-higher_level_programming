#!/usr/bin/python3

# Removes all characters c and C from a string.

def no_c(my_string):
    n_str = my_string.translate({ord('c'): None})
    n_str = n_str.translate({ord('C'): None})
    return n_str
