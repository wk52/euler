"""Project Euler - Problem 9."""


def find_triplet():
    """Return product(abc) where a + b + c = 1000 and a**2 + b**2 = c**2."""
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        return a * b * c
    return 0


print(find_triplet())
