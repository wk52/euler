"""Project Euler - Problem 20.

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def n_factorial(n):
    """Recursive function for n!."""
    if n == 1:
        return n
    else:
        return n * n_factorial(n - 1)


fac_100 = n_factorial(100)
sum_of_digits = 0

for digit in str(fac_100):
    sum_of_digits += int(digit)

print(sum_of_digits)
