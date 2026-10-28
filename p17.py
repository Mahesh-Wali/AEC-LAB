import numpy as np

# Given values
P_D = 0.02          # Probability of disease
P_positive_D = 0.95 # Sensitivity
P_positive_not_D = 0.04  # False-positive rate

# Bayes' Theorem
P_positive = (P_positive_D * P_D) + (P_positive_not_D * (1 - P_D))

P_D_positive = (P_positive_D * P_D) / P_positive

print("P(Disease | Positive) =", P_D_positive * 100, "%")