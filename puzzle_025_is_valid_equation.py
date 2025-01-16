#/usr/bin/env python3

def is_valid_equation(input_equation: str) -> bool:
    """
    This function checks if an equation is valid.
    :param: input_ equation: This is a string representing a simple
            equation with a single operator and two operand, an equals
            sign and an answer to be checked.
    :return: True if the equation is valid, False otherwise.

    NB: The actual puzzle question is worded in such a way that I feel
    that the expected answer was to split the input equation at the
    spaces and then check for a plus or minus sign at input_equation[1]
    as it states that the equation should only have a plus or minus 
    operand. However this solution allows a user to check all operands.
    and works for equations with more than 2 integers.
    """
    split_equation = input_equation.split('=')
    return eval(split_equation[0]) == int(split_equation[1])


# Example function calls
print(is_valid_equation('1 + 1 = 2'))
print(is_valid_equation('1 + 1 = 3'))
print(is_valid_equation('1 - 1 = 0'))
print(is_valid_equation('10 * 10 = 101'))
print(is_valid_equation('10 / 10 + 2 = 3'))
