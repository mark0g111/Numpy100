# Переменная M1 содержит Numpy матрицу.
# Произведите операции последовательно:
# 1. Замените значения в предпоследней строке на значения по формуле: sin((pi * x) / 6)
# 2. Замените значения в предпоследнем столбце на значения по формуле: e^x

import numpy as np

M1 = np.array((
    (1., 2., 3., 0.),
    (4., 5., 6., 0.),
    (0., 1., 1., 6.),
    (7., 8., 9., 0.)
))

M1[-2] = np.array((np.sin(np.pi * M1[-2] / 6)))
M1[:, -2] = np.array((np.e ** M1[:, -2]))
M2 = M1
