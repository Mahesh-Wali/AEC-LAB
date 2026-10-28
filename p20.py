import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

for lam in [1,3,5,10]:
    d=stats.poisson(lam)
    sim=np.random.poisson(lam,5000)
    
print(sim)