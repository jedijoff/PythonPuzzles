#!/usr/bin/env python3

def sum_even_numbers(list_of_numbers):
    """returns the sum of all even numbers in a list.

    :param list_of_numbers: a list of numbers passed to the function.
           via the function call: sum_even_numbers(list_of_numbers).
    """
    sum = 0
    for number in list_of_numbers:
        if number % 2 == 0:
            sum += number
    return sum


print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even_numbers([2, 4, 6, 8, 10]))
print(sum_even_numbers([1, 3, 5, 7, 9]))
print(sum_even_numbers([10, 20, 30, 40, 50]))
print(sum_even_numbers([15, 25, 35, 45, 55]))
