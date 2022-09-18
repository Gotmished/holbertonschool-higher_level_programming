#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    tot = 0
    string_length = len(roman_string)
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(string_length - 1):
        val = roman_dictionary.get(roman_string[i])
        if i <= string_length - 2:
            if val < roman_dictionary.get(roman_string[i + 1]):
                val = val * -1
            tot = tot + val
    return tot
