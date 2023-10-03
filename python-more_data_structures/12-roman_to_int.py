#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return None
    roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5,
                  "I": 1, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                  'CD': 400, 'CM': 900}
    number = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_dict:
            number += roman_dict[roman_string[i:i+2]]
            i += 2
        else:
            number += roman_dict[roman_string[i]]
            i += 1
    return number
