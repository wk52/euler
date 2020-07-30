"""Project Euler - Problem 5."""


def evenly_divisible(n, divisible_to):
    """Return True if n is evenly divisible by 1:divisible_to."""
    divisible = True  # assume true until proven false

    for i in range(1, divisible_to + 1):
        if n % i != 0:  # remainder found -> not evenly divisible
            divisible = False
            break
    return divisible


j = 2520
while not evenly_divisible(j, 20):
    j += 2520

print(j)
