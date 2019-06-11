n = int(input())
a,b=0,1
result = [0]
for i in range(n-1):
    result.append(b)
    a,b=b,a+b
print(result)