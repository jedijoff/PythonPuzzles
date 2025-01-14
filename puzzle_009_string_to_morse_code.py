#!/usr/bin/env python3

def string_to_morse_code(input_string):
    """ A function that converts a string to morse code

    Args:
        input_string: A string to be converted to morse code.
        The string can contain letters, numbers, and special
        characters.
    :return:
        A string containing the morse code translation of
        the input string.
    """
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' ',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
        '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
        '_': '..--.-', '"': '.-..-.', '$': '...-..-', '!': '-.-.--',
        '@': '.--.-.'
    }
    return ' '.join(morse_code.get(chr.upper(), chr) for chr in input_string)


# Example function calls:
print(string_to_morse_code('Hello, World!'))
print(string_to_morse_code('https://abc@xyz.net/python?query=string'))
