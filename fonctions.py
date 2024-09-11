#!/bin/python3


def puissance(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError as e:
        raise TypeError("Que des integer !!!")

    value = a if b >= 0 else 1/a
    for i in range(1, abs(b)):
        if b >= 0:
            value *= a
        else:
            value /= a

    return value

