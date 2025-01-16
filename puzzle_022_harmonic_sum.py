#/usr/bin/env python3

def harmonic_number(number):
    """
    This function calculates the nth harmonic number.

    This is a recursive function that calculates the nth harmonic number.
    The harmonic number is the sum of the reciprocals of the first n
    natural numbers. The first harmonic number is 1.

    :param: number: An integer number to represent the nth harmonic number.
    :return: the nth harmonic number.
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return 1 / number + harmonic_number(number - 1)

# Example function calls
print(harmonic_number(0))
print(harmonic_number(1))
print(harmonic_number(5))
print(harmonic_number(10))
print(harmonic_number(100))