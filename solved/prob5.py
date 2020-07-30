"""Project Euler - Problem 5.

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""


def evenly_divisible(n, divisible_to):
    """Return True if n is evenly divisible through 1:divisible_to."""
    for i in range(1, divisible_to + 1):
        if n % i != 0:  # remainder found -> not evenly divisible
            return False
    return True


smallest_number = 2520
while not evenly_divisible(smallest_number, 20):
    smallest_number += 2520

print(smallest_number)
