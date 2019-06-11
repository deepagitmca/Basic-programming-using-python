n = int(input())
b = 0
a = 1
result = [0]
for i in range(0,n):
    c=a+b
    a=b
    b=c
    result.append(c)
print(result)