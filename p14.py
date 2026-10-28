import numpy as np

# Sample space of two dice
dice1 = np.array([1, 2, 3, 4, 5, 6])
dice2 = np.array([1, 2, 3, 4, 5, 6])

sample_space = np.array(np.meshgrid(dice1, dice2)).T.reshape(-1, 2)

print("Sample Space:")
print(sample_space)

total = len(sample_space)

# a) Sum is 7
a = np.sum(sample_space[:, 0] + sample_space[:, 1] == 7)
print("a) Probability of sum 7:", a / total)

# b) Sum is greater than 8
b = np.sum(sample_space[:, 0] + sample_space[:, 1] > 8)
print("b) Probability of sum greater than 8:", b / total)

# c) Both dice show same number
c = np.sum(sample_space[:, 0] == sample_space[:, 1])
print("c) Probability of same number:", c / total)

# d) At least one die shows 6
d = np.sum((sample_space[:, 0] == 6) | (sample_space[:, 1] == 6))
print("d) Probability of at least one 6:", d / total)