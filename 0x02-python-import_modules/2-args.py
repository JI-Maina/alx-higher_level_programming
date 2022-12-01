#!/usr/bin/python3

if __name__ == '__main__':

    import sys

    x = len(sys.argv) - 1

    if x < 1:
        print("0 arguements.")
    elif x == 1:
        print("1 arguement:")
    else:
        print("{} arguements:".format(x))

    for i in range(x):
        print("{}: {}".format((i + 1), sys.argv[i + 1]))
