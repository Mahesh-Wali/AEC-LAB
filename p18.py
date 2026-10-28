import numpy as np

# Given values
P_spam = 0.20
P_offer_spam = 0.80
P_offer_not_spam = 0.10

# Probability of getting "offer"
P_offer = (P_offer_spam * P_spam) + (P_offer_not_spam * (1 - P_spam))

# Bayes theorem
P_spam_offer = (P_offer_spam * P_spam) / P_offer

print("P(Spam | offer) =", P_spam_offer * 100, "%")