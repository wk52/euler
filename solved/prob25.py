"""Project Euler - Problem 25.

What is the index of the first term in the Fibonacci
sequence to contain 1000 digits?
"""

sequence_terms = [0, 1]  # list with the first two terms

while len(str(sequence_terms[-1])) < 1000:
    term = sequence_terms[-1] + sequence_terms[-2]  # F(N) = F(N-1) + F(N-2)
    sequence_terms.append(term)

# print index of first term with 1000 digits
print(sequence_terms.index(sequence_terms[-1]))
