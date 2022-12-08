#!/usr/bin/python3

# Returns a new dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    dict = a_dictionary.copy()
    for i, j in enumerate(dict):
        j = j * 2
    return dict
