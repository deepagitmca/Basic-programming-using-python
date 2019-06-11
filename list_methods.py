st = input()
ch = list(st)
ch.sort()
rs = []
for c in ch:
    if c not in rs:
        rs.append(c)
print(rs)
