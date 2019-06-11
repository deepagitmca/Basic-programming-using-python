some_var = 1
def fib(n):
    """print fibonacci series up to n"""
    a,b=0,1
    while b < n:
        print(b,end=' ')
        a,b=b,a+b
fib(10)