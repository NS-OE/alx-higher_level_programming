#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    no = (number % 10) * -1
else:
    no = number % 10
if no > 5:
    print("Last digit of", number, "is", no, "and is greater than 5\n")
elif no == 0:
    print("Last digit of", number, "is", no, "and is 0\n")
elif no < 6 and no != 0:
    print("Last digit of", number, "is", no, "and is less  than 6 and not 0\n")
