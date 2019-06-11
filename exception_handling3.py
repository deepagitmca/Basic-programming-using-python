prompt = 'Enter a number : '
while True:
    try:
        x = int(input(prompt))
        break
    except ValueError:
        print("Invalid input, try again...")