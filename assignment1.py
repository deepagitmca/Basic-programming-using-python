import numpy
mt = map(int,row_input().split())
a = int(mt[0])
b = int(mt[1])
if(a==b):
    print(numpy.eye(a,b,k=0))
