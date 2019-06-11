prompt = "enter no."
while True:
    try:
        x = int(input(prompt))
        break
    except ValueError:
        print("Invalid input")
    finally:
        print("Finally")