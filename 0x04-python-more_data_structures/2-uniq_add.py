#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    number = 0

    unique_iterator = iter(uniq_list)
    while True:
        try:
            i = next(unique_iterator)
            number += i
        except StopIteration:
            break

    return (number)
