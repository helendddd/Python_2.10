#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calculating_multiply(*args):
    """
    Вычисление среднего геометрического полученных аргументов.
    """

    if args:
        multiply = 1.0
        for value in args:
            multiply *= value
        return round(pow(multiply, 1/len(args)), 2)
    else:
        return "None"


if __name__ == "__main__":
    elements = [1, 2, 8, 9, 2]
    print("Elements:", *elements)
    print("Geometric mean of elements: ", calculating_multiply(*elements))
    print(calculating_multiply())
