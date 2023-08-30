#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dir = a_dictionary.copy()
    keys_list = list(n_dir.keys())

    i = 0
    while i < len(keys_list):
        key = keys_list[i]
        n_dir[key] *= 2
        i += 1

    return (n_dir)
