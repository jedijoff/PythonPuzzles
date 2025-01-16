#/usr/bin/env python3

from typing import Any

def my_zip(input_list_a: list[Any], input_list_b: list[Any]) \
                                    -> list[tuple[Any, Any]]:
    """
    My veriosn of the built in zip function

    This function takes in an arbitrary number of iterables and returns
    an iterator of tuples. It will automatically stop when the shortest
    input iterable is exhausted.

    :param: input_list_a: any type of list object.
    :param: input_list_b: any type of list object.

    :return: A list of tuples in format [(a[0], b[0]),(a[1], b[1]) ...]
             The length of the returned list is equal to the shortest
             input list object.
    """
    length = min(len(input_list_a), len(input_list_b))
    return [(input_list_a[i], input_list_b[i]) for i in range(length)]


# Example function calls
print(my_zip([1, 2, 3], ["a", "b", "c"]))
print(my_zip((1, 2, 3), ("a", "b", "c", "d", "e")))
print(my_zip((1, 2, 3, 4, 5), ["a", "b", "c"]))
