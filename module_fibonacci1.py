some_var = 1
def fib(n):
    """print fibonacci series up to n"""
    a,b=0,1
    while b < n:
        print(b,end=' ')
        a,b=b,a+b
print(__name__)
if __name__ == '__main__':
    fib(10)