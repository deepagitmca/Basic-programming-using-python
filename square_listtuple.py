text = input()
result = []
for item in text.split():
    x = int(item)
    result.append((x,x*x))
print(result)

#iterating over a list of tuples
#data = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
#for x,y in data:
#   print(x,y)