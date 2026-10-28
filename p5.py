import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 16π
x = np.linspace(0, 16 * np.pi, 500)

# Compute sine values
y = np.sin(x)

# Plot the graph
plt.plot(x, y, label='y = sin(x)', color='blue', linewidth=2)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.title('Sine Function Graph')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()