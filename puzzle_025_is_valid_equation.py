#/usr/bin/env python3

def is_valid_equation(input_equation: str) -> bool:
    """
    This function checks if an equation is valid.
    :param: input_ equation: This is a string representing a simple
            equation with a single operator and two operand, an equals
            sign and an answer to be checked.
    :return: True if the equation is valid, False otherwise.
    """
    split_equation = input_equation.split('=')
    return eval(split_equation[0]) == int(split_equation[1])


# Example function calls
print(is_valid_equation('1 + 1 = 2'))
print(is_valid_equation('1 + 1 = 3'))
print(is_valid_equation('1 - 1 = 0'))
print(is_valid_equation('10 * 10 = 100'))
print(is_valid_equation('10 / 10 = 3'))
