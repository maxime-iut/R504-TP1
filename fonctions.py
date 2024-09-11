#!/bin/python3


def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("Que des integer !!!")

    return a ** b

