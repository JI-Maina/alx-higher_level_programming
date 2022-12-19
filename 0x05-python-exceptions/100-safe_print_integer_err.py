#!/usr/bin/python3

# A function that prints an integer.
# Returns True if value has been correctly printed (it means the value is an integer)

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end='')
    except Exception as arguement:
        print("Exception:", arguement)
        return False
    print()
    return True
