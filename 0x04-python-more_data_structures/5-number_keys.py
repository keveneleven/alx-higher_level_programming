#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    key_list = list(a_dictionary.keys())

    keys_iterator = iter(key_list)
    while True:
        try:
            key = next(keys_iterator)
            number += 1
        except StopIteration:
            break

    return (number)
