#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last digit = number % 10
print("Last digit of", end=' ')
print("number", end=' ')
print("is", end=' ')
if Last digit > 5:
    print(last digit "is greater than 5")
elif Last digit == 0:
    print(last digit "is 0")
else
    print(last digit "is less than 6 and not 0")
