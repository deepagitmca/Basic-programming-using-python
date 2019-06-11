from pylab import *
t=range(10000000)
t = array(t)
tsq = t*t
len(t)
print(t)
%timeit sqr(t)
%timeit t*t