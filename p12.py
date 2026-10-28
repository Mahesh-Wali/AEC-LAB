import numpy as np

# Sample space for 3 coin tosses
sample_space = np.array([
    "HHH", "HHT", "HTH", "HTT",
    "THH", "THT", "TTH", "TTT"
])

print("Sample Space:")
print(sample_space)

# Total outcomes
total = len(sample_space)

# a) Exactly 3 Heads
exactly_3 = np.array([x.count("H") == 3 for x in sample_space])
p3 = np.sum(exactly_3) / total

# b) Exactly 2 Heads
exactly_2 = np.array([x.count("H") == 2 for x in sample_space])
p2 = np.sum(exactly_2) / total

# c) At least 1 Head
at_least_1 = np.array([x.count("H") >= 1 for x in sample_space])
p1 = np.sum(at_least_1) / total

print("Probability of exactly 3 Heads:", p3)
print("Probability of exactly 2 Heads:", p2)
print("Probability of at least 1 Head:", p1)