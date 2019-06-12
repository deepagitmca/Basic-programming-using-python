#store the nae and value as entered number and its square (enter number with spaces)
st = input()
d = {}
for item in st.split():
    x = int(item)
    d[item] = x*x
print(d)