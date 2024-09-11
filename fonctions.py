#!/bin/python3


def puissance(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError as e:
        raise TypeError("Que des integer !!!")

    return a ** b

