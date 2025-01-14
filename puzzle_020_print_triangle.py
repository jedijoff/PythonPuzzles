#!/usr/bin/env python3

def print_triangle(number_of_levels: int, symbol: str):
    """
    Function prints a triangle of a given symbol.

    :param number_of_levels: the number of rows in the triangle.
    :param symbol: the symbol to be used in the triangle.
    :return: None
    """
    spaces = ' ' * (number_of_levels -1)
    symbols = 1
    for i in range(1, number_of_levels + 1):
        print(f'{spaces}{symbol * symbols}')
        spaces = spaces[:-1]
        symbols += 2


# Example function calls:
print_triangle(4, '*')
print_triangle(10, 'A')
print_triangle(5, '+')