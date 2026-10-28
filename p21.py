import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from scipy import stats
np.random.seed(42)
n,p=20,0.35
binom=stats.binom(n,p)
x=np.arange(0,n+1)
print(f'Mean={binom.mean():.4f} (Theory:np={n*p})')
print(f'Variance={binom.var():.4f} (Theory:npq={n*p*(1-p)})')
print(f'Standard Deviation={binom.std():.4f} (Theory:sqrt(npq))')
binom.var()
binom.moment(2)
binom.stats("s")
binom.cdf(10)
binom.pmf(7)
# Poisson Distribution
for lam in [1,3,5,10]:
  d=stats.poisson(lam)
  sim=np.random.poisson(lam,5000)