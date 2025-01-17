from typing import Any

def rotate_list_left(input_list: list[Any], rotate_amount: int) -> list[Any]:
    """
    This function rotates a list to the left by a specified amount.

    :param input_list: A list of any type of object
    :param rotate_amount: An integer representing the number of places
           to rotate the list. It does not matter if the number is
           greater than the length of the list as this is handled
           automatically.
    :return: the rotated list.
    """
    rotate_amount %= len(input_list)
    return input_list[rotate_amount:] + input_list[:rotate_amount]


# Example function calls
print(rotate_list_left([1, 2, 3, 4, 5], 2))
print(rotate_list_left([1, 2, 3, 4, 5], 7))
print(rotate_list_left(['a', 2, (1, 2, 3), 4, 5], 3))
