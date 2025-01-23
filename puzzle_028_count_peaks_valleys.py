#!/usr/bin/env python3

def count_peaks_valleys(price_action: list[int]) -> tuple[int, int]:
    """
    Function that counts peaks and troughs in a given list of values.

    :param: price_action: This is the original list passed to
                         the function.
    :return: a human readable tuple of the number of peaks and
             the number of troughs in the values provided.
    """
    peaks = 0
    valleys = 0
    check_list = price_action[1:-1]

    for x in range(len(check_list)):
        pos_plus_1 = price_action[x + 2]
        pos_minus_1 = price_action[x]

        if check_list[x] > pos_minus_1 and check_list[x] > pos_plus_1:
            peaks += 1
        elif check_list[x] < pos_minus_1 and check_list[x] < pos_plus_1:
            valleys += 1

    return (f'Peaks = {peaks}', f'Valleys = {valleys}')


# Example function calls
print(count_peaks_valleys([1, 2, 3, 4, 3, 2, 1]))
print(count_peaks_valleys([1, 2, 3, 2, 1, 2]))
print(count_peaks_valleys([7, 6, 5, 10, 11, 12, 10, 9, 10]))
