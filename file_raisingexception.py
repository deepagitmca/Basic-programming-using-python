def func(x):
   if type(x) != int:
       raise TypeError('Expected int')
   elif x < 0:
        raise ValueError('Got negative int')
    
print(func('a')) #output: TypeError: Expected int
print(func(6)) #output: None