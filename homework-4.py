# William Chase Hamby
# 3/2/20
# homework-4.py
# -*- coding: utf-8 -*-
# This is the description for homework 4

import random


random_number = random.randint(1, 10)
guess = None
attempts = 0

while random_number != guess:
    guess = int(input("Step right up! Pick a number, any number between 1 and 10."))
    attempts += 1
    # This is the basically the splash text you see first
    
    if random_number == guess:
        print("\nYou guessed the number! Congratulations! The number was", random_number)
        # The response you will get if you guess the number
        # The response you will get if the number is higher
    elif guess < random_number:
        print("Higher...")
        # The response you will get if the number is lower
    elif guess > random_number:
        print("Lower...")
