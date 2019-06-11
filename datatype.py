a = 13
print(a)
b = 999999999999999999999999
print(b)
p = 3.141592
print(p)
c = 3+4j
print(c)
c = complex(3,4)
print(c)
t = True
F = not t
print(F or t)
print(F and t) 
a = False
b =True
c = True
print((a and b) or c)
print(a and(b or c))
print(a and b or c)
print(a and b or c)
print('Hello')
print("Hello")
print("""Hello""")
print('''Hello''')
print('"Hello"world')
print(""" Hello
           world """)
w = "hello"
print(w[0],w[1],w[-1])
print(len(w))
#w[0] = 'H' #TypeError: 'str' object does not support item assignment (String are immutable)
a = 1.0
print(type(a))
print(type(1))
print(1786%12)
print(45%2)
print(864675%10)
print(3124*1236789)
big = 123456789123456789 ** 3 #power
print(big)
verybig = big * big * big * big
print(verybig)
print(17/2)
print(17/2.0)
print(17.0/2)
print(17.0/8.5)

 #tKE CODE
a = 'Hello World'
print(a.startswith('Hell'))
print(a.endswith('ld'))
print(a.upper())
print(a.lower())
a = '   Hello World    '
b = a.strip()
print(b)

#print(b.index('1=ll'))
print(b.replace('Hello','Good'))

chars = 'a b c'
print(chars.split())
' '.join(['a','b','c'])
alpha = ', '.join(['a','b','c'])
print(alpha)
print(alpha.split(', '))
