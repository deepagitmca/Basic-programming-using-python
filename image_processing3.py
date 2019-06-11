from numpy import*
from pylab import*
import numpy
a = imread('lena.png')
imshow(a)
print(a.shape)
print(a.dtype)
rank(a)
b = a[::2,::2]
print(b.shape)
imshow(b)
show()