#!/usr/bin/python3

# Returns a set of common elements in two sets.

def common_elements(set_1, set_2):
    list = set(set_1 & set_2)
    return list
