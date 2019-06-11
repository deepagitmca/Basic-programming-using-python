a,b=0,1
while b < 500:
    if b % 4 == 0 and b > 8:
        print(b)
        break
    a,b=b,a+b        