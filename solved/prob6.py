"""Project Euler - Problem 6.

https://projecteuler.net/problem=6"""

sum_of_squares = 0
for i in range(1, 101):
    sum_of_squares += i**2

SUM = 0
for j in range(1, 101):
    SUM += j

square_of_sum = SUM**2

print(square_of_sum - sum_of_squares)
