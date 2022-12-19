#!/usr/bin/python3

# A function that divides 2 integers and prints the result.
# Returns the value of the division, otherwise: None

def safe_print_division(a, b):
    try:
        x = a / b
    except (TypeError, ZeroDivisionError):
        x = None
    finally:
        print("Inside result: {}".format(x))
    return x
