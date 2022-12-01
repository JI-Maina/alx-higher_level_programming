#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    x = len(sys.argv) - 1

    if x < 1:
        print("0 arguements.")
    elif x == 1:
        print("{} arguement:".format(x))
        print("{}: {}".format(x, sys.argv[1]))
    else:
        print("{} arguements:".format(x))
        for i in range(len(sys.argv)):
            if i >= 1:
                print("{}: {}".format(i, sys.argv[i]))
