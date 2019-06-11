a = input()
e = int(a)
b = e//100 #double // is used to convert floating numbet to whole number 12.9 to 13
c = (e%100)//10
d = e%10
if(b**3 + c**3 + d**3 == e):
    print("armstrong number")
else:
    print("Not armstrong")
    


