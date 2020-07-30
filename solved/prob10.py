"""Project Euler - Problem 10."""

from math import sqrt


def is_prime(n):
    """Return True if n is prime."""
    prime = True  # assume prime until proven false

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:  # multiple found -> not prime
            prime = False
            break
    return prime


primes_sum = 0
j = 2  # start with first prime

while j < 2000000:
    if is_prime(j):
        primes_sum += j
    j += 1

print(primes_sum)
