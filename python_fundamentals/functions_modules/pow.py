#!/usr/bin/env python3

def pow(a, b):
    result = 1
    negative = b < 0
    b = abs(b)

    for i in range(b):
        result = result * a

    if negative:
        return 1 / result

    return result
