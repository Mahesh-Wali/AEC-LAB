import numpy as np
result=np.random.choice(["farhaan","mahesh"],size=10000)
print(result)
heads=np.sum(result=="mahesh")
print("mahesh :",heads)
print("probability of mahesh: ",heads/10000)

