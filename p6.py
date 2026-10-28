import numpy as np
import pandas as pd


number_of_rolls = 1000
rng = np.random.default_rng()

# Generate integers from 1 through 6, inclusive.
rolls = rng.integers(1, 7, size=number_of_rolls)

results = pd.DataFrame({"Roll": rolls})
frequency_table = (
	results["Roll"]
	.value_counts()
	.reindex(range(1, 7), fill_value=0)
	.rename_axis("Face")
	.reset_index(name="Frequency")
)
frequency_table["Relative Frequency"] = (
	frequency_table["Frequency"] / number_of_rolls
)

print("First 10 rolls:")
print(results.head(10).to_string(index=False))
print("\nDice frequency table:")
print(frequency_table.to_string(index=False))
