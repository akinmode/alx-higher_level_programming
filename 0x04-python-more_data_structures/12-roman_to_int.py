#!/usr/bin/python3
def roman_to_int(roman_string):
    """
        Converts a Roman numeral to an integer.
    """
    if roman_string is not None and type(roman_string) is str:
        roman_dict = {"I": 1, "V": 5, "X": 10,
                      "L": 50, "C": 100, "D": 500, "M": 1000}
        numbers = [roman_dict[x] for x in roman_string]
        if numbers != []:
            int_res = 0
            prev_pos = 1000
            for x in numbers:
                if x > prev_pos:
                    int_res -= prev_pos * 2
                prev_pos = x
                int_res += x
            return int_res
    else:
        return 0
