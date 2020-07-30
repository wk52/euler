"""Project Euler - Problem 8 (1000-digit number stored in prob8.txt)."""

import re

f = open("prob8.txt", "r")

number: str = re.sub('[^0-9]', '', f.read())  # remove non-numeric chars

largest_product = 0
for i in range(len(number) - 13):
    product = 1
    for j in range(13):
        product *= int(number[i + j])
        if product > largest_product:
            largest_product = product

print(largest_product)
