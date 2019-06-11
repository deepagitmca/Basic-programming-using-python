data = input()
try:      
    x = int(data.split(',')[1])
except (ValueError,IndexError):
        print("Input atleast 2 values")
