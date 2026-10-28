
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

# Probability of success
p_geo = 0.3

# Trial numbers (1 to 19)
x_g = np.arange(1, 20)

# Create Geometric Distribution
geo = geom(p_geo)

# Visualization - Geometric PMF
plt.figure(figsize=(7, 5))

plt.bar(
    x_g, geo.pmf(x_g),
    color='green',
    edgecolor='black',
    alpha=0.8
)

plt.title(f'Geometric PMF (p={p_geo})')
plt.xlabel('Trial Number (x)')
plt.ylabel('Probability')
plt.xticks(x_g)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
