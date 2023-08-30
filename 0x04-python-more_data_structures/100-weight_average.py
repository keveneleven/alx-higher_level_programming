#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    i = 0
    while i < len(list_keys):
        key = list_keys[i]
        new_dir[key] *= 2
        i += 1

    return (new_dir)
