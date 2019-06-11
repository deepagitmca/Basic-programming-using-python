prompt = 'Enter a number(Q to quit):'
a = input(prompt)
try:
    num = int(a)
    print(num)
except:
    if a == 'Q':
        print("Exiting....")
    else:
        print("Wrong input...")