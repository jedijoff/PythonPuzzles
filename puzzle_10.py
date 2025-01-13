def second_largest_number(numbers: list):
    """ A function that returns 2nd largest number from a list of numbers

    Args:
        list_of_numbers: A list of integer numbers. The list must contain
        a minimum of 2 numbers"""
    unique_numbers = list(set(numbers))
    return (sorted(unique_numbers)[-2]) if len(unique_numbers) > 1 else None


print(second_largest_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(second_largest_number([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(second_largest_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(second_largest_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
print(second_largest_number([1, 1, 1, 1, 1, 1, 1, 2, 2, 2]))