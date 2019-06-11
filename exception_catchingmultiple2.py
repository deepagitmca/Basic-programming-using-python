while True:
    try:
        data = input()
        x = int(data.split(',')[1])
    except (ValueError,IndexError):        #raise ValueError("error message") <------ use this to raise error ...try this on command prompt
        print("Invalid input...")
    else:
        print("All is well")
        break