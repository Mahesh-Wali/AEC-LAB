import numpy as np

# Sample space
die = np.array([1, 2, 3, 4, 5, 6])

# A = even number
A = die % 2 == 0

# B = number greater than 3
B = die > 3

# A and B
A_and_B = A & B

# P(A|B) = P(A and B) / P(B)
P_A_given_B = np.sum(A_and_B) / np.sum(B)

print("P(A|B) =", P_A_given_B)