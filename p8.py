import numpy as np

rolls=np.random.randint(1,7,10)
for number in range(1,7):
    count = np.sum(rolls==number)
    probability=count/10
    print("number=",number,"count=",count,"probability=",probability)