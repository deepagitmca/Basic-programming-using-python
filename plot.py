from pylab import *
time=[0.,1.,2.,3]
distance=[7.,11,15,19]
plot(time,distance)
xlabel('time')
ylabel('distance')
clf()
plot(time,distance,'o')
clf()
plot(time,distance,'.')
clf()
plot(time,distance,'-')
clf()
plot(time,distance,'--')
clf()
plot(time,distance,'*')
show()
