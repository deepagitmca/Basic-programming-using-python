while True:
    try:
        data = input()
        x = int(data.split(',')[1])
        break
    except IndexError:
        print("Input atleast 2 values")
    except ValueError:
        print("Invalid input,try again")