def remove_vowels(input_string):
    vowels = "aeiou"
    return "".join([char for char in input_string if char.lower() not in vowels])


print(remove_vowels("Apple"))
print(remove_vowels("banana"))
print(remove_vowels("cherry"))
print(remove_vowels("Hello world"))
print(remove_vowels("Echo"))
