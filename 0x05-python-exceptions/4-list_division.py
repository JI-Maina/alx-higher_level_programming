#!/usr/bin/python3

# A function that divides element by element 2 lists.
# Returns a new list (length = list_length) with all divisions

def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            x = 0
            print("division by 0")
            continue
        except TypeError:
            x = 0
            print("wrong type")
            continue
        except IndexError:
            x = 0
            print("out of range")
        finally:
            list.append(x)
    return list
