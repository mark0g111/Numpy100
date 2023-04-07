import numpy as np
Z = np.array([1,2,3], dtype=np.float64)

print(Z.itemsize * len(Z))

print(Z.nbytes)

# Z.itemsize * len(Z) == Z.nbytes
