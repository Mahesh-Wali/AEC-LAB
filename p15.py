import numpy as np
import matplotlib.pyplot as plt

# 10,000 coin tosses
tosses = np.random.randint(0, 2, 10000)

# Cumulative probability of Heads
heads = np.cumsum(tosses)
toss_number = np.arange(1, 10001)
probability = heads / toss_number

# Plot
plt.plot(toss_number, probability)
plt.axhline(0.5, linestyle='--')

plt.xscale('log')
plt.xlabel("Number of Tosses")
plt.ylabel("Cumulative Probability of Heads")
plt.title("Law of Large Numbers")
plt.show()