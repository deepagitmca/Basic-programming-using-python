import numpy as np
data = [1.0,4.5,2.3,-0.5,0.5,2.8] #data = np.array([1.0,4.5,2.3,-0.5,0.5,2.8])
print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.var(data))
print(np.std(data,ddof=1)) #increases compared to std denominator is setted
data = (print(data.sort))
md = np.arange(16) #arrange 16 no. from 0-15
md.shape = 4,4 #print 4x4 matrix
print(md)
print(np.mean(md))
print(np.std(md))
print(np.mean(md, axis=0)) #show the mean of matrix column wise  
print(np.mean(md, axis=1))
print(np.nan+1) #NaN means not a number output will be nan
data1 = [1.0,2.1,np.nan,3.0] #np.nan represent there is no number  ..... try np.nan<TAB> (hit tab) on terminal.... you will get all methods available
print(np.mean(data1),np.std(data1))
print(np.nanmean(data1)) #check output