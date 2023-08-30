#!/usr/bin/python3
def to_subtract(list_number):
    to_sub = 0
    max_list = max(list_number)

    for n in list_number:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    number = 0
    last_rom = 0
    list_number = [0]

    for ch in roman_string:
        for r_number in list_keys:
            if r_number == ch:
                if rom_n.get(ch) <= last_rom:
                    number += to_subtract(list_number)
                    list_number = [rom_n.get(ch)]
                else:
                    list_number.append(rom_n.get(ch))

                last_rom = rom_n.get(ch)

    number += to_subtract(list_number)

    return (number)
