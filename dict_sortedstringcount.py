# program convert string to lowercase and count character accurance in string
st = input().lower()
result = {}
for char in st:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
for char in sorted(result):
    print(char,result[char])