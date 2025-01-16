#!/usr/bin/env python3

def fibonacci(number):
    """
    This function calculates the nth number in the Fibonacci sequence.

    This is a recursive function that calculates the nth number in the
    Fibonacci sequence. The Fibonacci sequence is a series of numbers in
    which each number is the sum of the two preceding ones. The first
    two numbers in the sequence are 0 and 1.

    :param: number: An integer number to represent the nth number in
    the Fibonacci sequence.
    :return: the nth number in the Fibonacci sequence.
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


# Example function calls
print(fibonacci(10))
print(fibonacci(5))
print(fibonacci(0))