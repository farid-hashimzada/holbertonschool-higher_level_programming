#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if (last_digit > 5):
    print(f"and is greater than {last_digit}")
elif (last_digit == 0):
    print(f"and is 0 {last_digit}")
else:
    print(f"and is less than {last_digit} and not 0")
