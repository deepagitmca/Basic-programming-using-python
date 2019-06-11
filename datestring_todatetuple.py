#program to accept string and convert it into tuple i/p 24 june 2005 o/p (2005, 6, 24)
m = ('jan feb mar apr may jun jul' + 'agu sep oct nov dec').split()
m1 = {}
for i, m in enumerate(m):
    m1[m] = i + 1
d = input()
d = d.replace(',',' ')
d,m2,y=d.split()
dd,yyyy=int(d),int(y)
m3 = m2[:3].lower()
mm = m1[m3]
print((yyyy,mm,dd))