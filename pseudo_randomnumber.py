#creating histogram by generating random array ... remove comments from show to display graph
import numpy as np #type np.random? on terminal to check documnetation
#np.random.*
data = np.random.random(5)
print(data)
x = np.random.random((3,3))
print(x.shape)
#randint(low,high,size=5)
print(np.random.randint(-5,10,size=5))
print(np.random.randint(-5,10,size=(5,5)))
#loc:mean,scale:std-dev
print((np.random.normal(loc=0.0,scale=1.0,size=5)))
data1=np.random.normal(size=10000)
from matplotlib import pyplot as plt
plt.hist(data1);
plt.show()
data2=np.random.normal(size=20)
plt.hist(data2)
plt.hist(data2,bins=6)
plt.show()
data3=np.random.normal(size=100000)
plt.hist(data3,normed=True) #normed is used for normalization 
plt.hist(data3,bins=50,cumulative=True)
plt.show()
data4=np.random.poisson(lam=0.5,size=100000) #lam is lamda
ax1 = plt.subplot(1,2,1)
ax1.hist(data4,normed=True)
plt.show()
ax2 = plt.subplot(1,2,1)
ax2.hist(data4,cumulative=True)
plt.show()
for i in range(1,5):
    ax = plt.subplot(2,2,i)
    ax.text(0.0,0.5,'plot number %d'%i)
    plt.show()
    
