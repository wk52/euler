"""Project Euler - Problem 7."""

from math import sqrt


def is_prime(n):
    """Return True if n is prime."""
    prime = True  # assume prime until proven false

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:  # multiple found -> not prime
            prime = False
            break
    return prime


primes = []  # list to store generated primes
j = 2  # start with first prime
while len(primes) < 10001:
    if is_prime(j):
        primes.append(j)
    j += 1

print(primes[-1])  # 10001st prime
