#!/usr/bin/python3

# Returns a set of all elements present in only one set.

def only_diff_elements(set_1, set_2):
    list = set(set_1 ^ set_2)
    return list
