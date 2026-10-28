
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 20       # Number of trials
p = 0.05      # Probability of success

# Values of x (number of successes)
x = np.arange(0, n + 1)

# Create binomial distribution
pmf = binom.pmf(x, n, p)

# 1. Binomial PMF
plt.figure(figsize=(7, 5))

plt.bar(
    x, pmf,
    color='steelblue',
    edgecolor='black',
    alpha=0.8
)

plt.axvline(
    binom.mean(n, p),
    color='red',
    linestyle='--',
    label=f'Mean = {binom.mean(n, p):.1f}'
)

plt.title(f'Binomial PMF (n={n}, p={p})')
plt.xlabel('Number of Successes (x)')
plt.ylabel('Probability')
plt.xticks(x)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
