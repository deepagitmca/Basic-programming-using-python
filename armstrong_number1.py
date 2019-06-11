x = 100
while x < 1000:
    b = x//100 #double // is used to convert floating numbet to whole number 12.9 to 13
    c = (x%100)//10
    d = x%10
    if(b**3 + c**3 + d**3 == x):
        print(x)
    x += 1


