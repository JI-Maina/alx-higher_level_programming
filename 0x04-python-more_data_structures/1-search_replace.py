#!/usr/bin/python3

# Replaces all occurrences of an element by another in a new list

def search_replace(my_list, search, replace):
    list = my_list.copy()
    for i in range(len(list)):
        if list[i] == 2:
            list[i] = 89
    return list
