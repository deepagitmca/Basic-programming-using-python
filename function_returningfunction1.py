# closure f stores the value of n
def power2(n=2):
      def result(x):
          return n ** x
      return result
         

p2 = power2(2)
p3 = power2(3)
print(p2)
print(p3)
