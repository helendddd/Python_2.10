#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_before_last_positive(*args):
    """
    Функция находит сумму аргументов,
    расположенных до последнего положительного аргумента.
    """
    if not args:
        return None

    last_positive_index = -1

    for i, arg in enumerate(args):
        if arg > 0:
            last_positive_index = i

    if last_positive_index == -1:
        return None

    return sum(args[:last_positive_index])


if __name__ == "__main__":
    result = sum_before_last_positive(1, 3, -2, 3, 4, -5, 6)
    print("Sum before last positive elements ", result)
