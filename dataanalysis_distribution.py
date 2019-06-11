#ceating chisquare distribution
import numpy as np
from matplotlib import pyplot as plt
data = np.random.chisquare(7,size=10000)
ax1 = plt.subplot(1,2,1)
ax1.hist(data,normed=True)
plt.show()
ax2=plt.subplot(1,2,2)
ax2.hist(data,cumulative=True)
plt.show()