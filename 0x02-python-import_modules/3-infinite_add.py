#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    x = len(sys.argv) - 1
    add = 0

    for i in range(x):
        add += (int(sys.argv[i + 1]))
    print("{:d}".format(add))
