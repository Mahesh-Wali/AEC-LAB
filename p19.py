import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n,p=20,0.35
binom=stats.binom(n,p)
x=np.arange(0,n+1)
print(x)
