prompt = 'Enter a number(Q to quit):'
a = input(prompt)
try:
    num = int(a)
    print(num)
except ValueError:                       #ValueError built in exception
    if a == 'Q':
        print("Exiting....")
    else:
        print("Wrong input...")