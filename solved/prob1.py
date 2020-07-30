"""Project Euler - Problem 1."""

multiple_sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:  # multiple of 3 or 5 -> add to sum
        multiple_sum += i

print(multiple_sum)
