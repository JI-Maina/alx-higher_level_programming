#!/usr/bin/python3
def uppercase(str):
    for i in len(str):
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:
            print("str[i]", end="")
        else:
            str[i] = ord(str[i] - 32)
            print(f"str[i]", end="")
uppercase("best")
uppercase("Best School 98 Battery street")
