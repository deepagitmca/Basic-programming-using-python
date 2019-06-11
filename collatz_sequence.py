a = input()
b = int(a)
c = 0
while b != 1:
    if b%2==0:
        b = b//2 #double // is used to convert floating numbet to whole number 12.9 to 13   
    else:
        b = b * 3 + 1
    print(b)