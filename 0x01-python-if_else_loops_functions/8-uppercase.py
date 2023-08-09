#!/usr/bin/python3
def uppercase(input_str):
    index = 0
    while index < len(input_str):
        char = input_str[index]
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
        index += 1
    print("")
