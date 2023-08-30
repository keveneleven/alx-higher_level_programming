#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    i = 0
    while i < len(list_keys):
        key = list_keys[i]
        if value == a_dictionary.get(key):
            del a_dictionary[key]
        else:
            i += 1

    return (a_dictionary)
