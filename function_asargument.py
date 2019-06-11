def f(x):
    return 2*x
def apply(f,data):
    result = []
    for x in data:
        result.append(f(x))
    return result
print(apply(f,[1,2,3]))
