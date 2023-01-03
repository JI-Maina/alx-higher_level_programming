#!/usr/bin/python3


def text_indentation(text):
    if isinstance(text, str) == False:
        raise TypeError('text must be a string')

    list = ['.','?',':']

    for word in text:
        if word in list:
            print(word, end="")
            print()
            print()
        else:
            print(word, end="")
