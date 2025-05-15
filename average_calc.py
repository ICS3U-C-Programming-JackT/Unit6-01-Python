#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 13th, 2025

# Average calculator program in python

import random
import os


def main():

    # Initialize grades
    grades = []

    # Append 10 random numbers 1-100
    for i in range(10):
        new = random.randrange(1, 100)
        print(new, "added to array!")
        grades.append(new)

    # Initialize average
    average = 0

    # Loop through grades, add to average variable
    for i in grades:
        average += i / len(grades)

    # Display average
    print("Your average is: {:.2f}".format(average))


if __name__ == "__main__":
    main()
