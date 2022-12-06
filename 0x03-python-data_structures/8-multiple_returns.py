#!/usr/bin/python3

# Returns a tuple with the length of a str and its first char

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        res = (length, sentence[0:1])
        return res
