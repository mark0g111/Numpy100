import numpy as np

n = int(input())
m = int(input())
k = int(input())
shape = [m, k]
Z = np.array([i for i in range(n)])
Z = np.reshape(Z, shape)
print(Z)

