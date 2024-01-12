#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculating_garmonical(*args):
    """
    Вычисление среднего гармонического полученных аргументов.
    """

    if args:
        garmony = 0
        for value in args:
            garmony += 1 / value
        return round(len(args)/garmony, 2)
    else:
        return "None"


if __name__ == "__main__":
    elements = [1, 2, 8, 9, 2]
    print("Elements: ", *elements)
    print("Harmonic mean of elements: ", calculating_garmonical(*elements))
    print(calculating_garmonical())
