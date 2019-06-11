def what(x,n):
    if n < 0:
        n = -n
        x = 1.0/x
    z = 1.0
    while n > 0:
        if n % 2 == 1:
            z *= x
        x *= x
        n //= 2
    return z
        