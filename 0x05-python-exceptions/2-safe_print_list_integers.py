#!/usr/bin/python3

# A function that prints the first x elements of a list & only integers
# Returns the real number of integers printed

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (TypeError, ValueError, IndexError):
            continue
    print()
    return count
