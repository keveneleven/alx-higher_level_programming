#!/usr/bin/python3
letter = 97

while letter <= 122:
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
        letter += 1

