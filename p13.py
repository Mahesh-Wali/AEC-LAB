import numpy as np

# Sample space of a die
die = np.array([1, 2, 3, 4, 5, 6])

total = len(die)

# a) Even number
even = np.sum(die % 2 == 0)
print("Probability of even number:", even / total)

# b) Odd number
odd = np.sum(die % 2 != 0)
print("Probability of odd number:", odd / total)

# c) Number greater than 4
greater_4 = np.sum(die > 4)
print("Probability of number greater than 4:", greater_4 / total)

# d) Number less than or equal to 3
less_equal_3 = np.sum(die <= 3)
print("Probability of number <= 3:", less_equal_3 / total)