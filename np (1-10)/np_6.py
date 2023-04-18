import numpy as np

n = int(input())
x = int(input())

M = np.zeros(n)
M[x] = 1
print(M)
