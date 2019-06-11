a,b=0,1
while b < 500:
    if b%4==0:
        print(b,end=' ')
        break
    a, b=b, a+b
