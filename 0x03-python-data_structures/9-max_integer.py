#!/usr/bin/python3

# Finds the biggest integer of a list.

def max_integer(my_list=[]):
    if my_list == []:
        return
    my_list.sort()
    return my_list[-1]
