#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_list = list(a_dictionary.keys())
    order_list.sort()

    i = 0
    while i < len(order_list):
        key = order_list[i]
        value = a_dictionary.get(key)
        print("{}: {}".format(key, value))
        i += 1
