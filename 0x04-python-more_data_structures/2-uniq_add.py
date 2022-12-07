#!/usr/bin/python3

# Adds all unique integers in a list (only once for each integer)

def uniq_add(my_list=[]):
    list = set(my_list)
    sum = 0
    for item in list:
        sum += item
    return sum
