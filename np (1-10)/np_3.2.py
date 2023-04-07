import numpy

s = input().split()
if len(s) > 1 and s[-1].isalpha():
    shape = list(map(int, s[:-1]))
    dtype = s[-1]
else:
    shape = list(map(int, s))
    dtype = numpy.float64
Z = numpy.zeros(shape=shape, dtype=dtype)
