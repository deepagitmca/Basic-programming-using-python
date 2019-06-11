#program that take function and argument as parameter 
def safe_run(f,x):
    try:
        f(x)
    except ValueError:
        return 'ValueError'
    except TypeError:
        return 'TypeError'
    else:
        return 'Ok'
        
print(safe_run(float,'a')) #this will try to typecast f to float which gives error
print(safe_run(float,6))     
print(safe_run(6,6))  