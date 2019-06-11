n = int(input())
b = 0
a = 1
for i in range(0,n): #range take starting and ending value
    c=a+b
    a=b
    b=c
    if(c%4 == 0 and c > 8 and c < 500):
        print(c)        