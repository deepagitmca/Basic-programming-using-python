n = int(input())
b = 0
a = 1

for i in range(0,n): #range take starting and ending values
    print(b,end=' ')
    c=a+b
    a=b
    b=c
