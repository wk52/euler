"""Project Euler - Problem 3.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt


def is_prime(n):
    """Return True if n is prime."""
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:  # multiple found -> not prime
            return False
    return True


largest_prime_factor = 0
test_number = 600851475143

# find largest_prime_factor of test_number
for j in range(2, int(sqrt(test_number) + 1)):
    if test_number % j == 0:  # factor found -> check if prime
        if is_prime(j):
            if j > largest_prime_factor:
                largest_prime_factor = j

print(largest_prime_factor)
