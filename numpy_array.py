from numpy import*
from pylab import*
import numpy
x = linspace(0,1)
x = numpy.linspace(0,1)
plot(x,sin(x))
show()

#numpy array
a = array([1,2,3,4])
b = array([2,3,4,5])
print(a[0],a[-1])
print(a+b,a-b,a/b)
x = linspace(0.0,10.0,200)
x*=2*pi/10
#apply function on array
y=sin(x)
y=cos(x)
x[0]=-1
print(x[0],x[-1])
x = array([1.,2,3,4])
print(size(x))
print(x.dtype)
print(x.shape)
print(rank(x))
print(x.itemsize)

#multidimensional array
a = array([[0,1,2,3],[10,11,12,13]])
a.shape
a[1,3]
a[1,3]=-1
a[1]
a[1]=0

x = loadtxt('pendulum.txt')
x.shape

mean(L)
std(L)