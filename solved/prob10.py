"""Project Euler - Problem 10.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt


def is_prime(n):
    """Return True if n is prime."""
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:  # multiple found -> not prime
            return False
    return True


sum_of_primes = 0
j = 2  # start with first prime

while j < 2000000:
    if is_prime(j):
        sum_of_primes += j
    j += 1

print(sum_of_primes)
