def what(n):
    i = 1
    while i * i < n:
        i += 1
    return i * i == n,i