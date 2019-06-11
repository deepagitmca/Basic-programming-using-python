def fib(n=8):
      a,b=0,1
      result = []
      for i in range(n-1):
          result.append(b)
          a,b=b,a+b
      return result
         

print(fib(4))
print(fib())