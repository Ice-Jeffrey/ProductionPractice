from sklearn import preprocessing
import numpy as np

x=[1,2,3,4,5]
x_scaled = preprocessing.scale(x)
print(x_scaled)
for i in range(1,11):
    print(i)