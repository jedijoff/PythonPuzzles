def second_largest_number(numbers: list):
    """
    Function returns 2nd largest number from a list of numbers

    :param:
        numbers: A list of numbers. The list must contain
        a minimum of 2 numbers
    :return:
        The 2nd largest number from the list of numbers.
        If the list contains less than 2 numbers, the function
        returns None.
    """
    unique_numbers = list(set(numbers))
    return (sorted(unique_numbers)[-2]) if len(unique_numbers) > 1 else None


print(second_largest_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(second_largest_number([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(second_largest_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(second_largest_number([1, 1, 1, 1, 1, 1, 1, 2, 2, 2]))
print(second_largest_number([1.25, 1.5, 1.75, 3.25, 2.0, 2.25,
                             2.5, 2.75, 3.0, 3.5]))