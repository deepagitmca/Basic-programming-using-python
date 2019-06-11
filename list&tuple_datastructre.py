#square add numbers
n = int(input())
result = []
for i in range(1,n-1,2):
    result.append(i*i)
resultt = tuple(result)
print(resultt)