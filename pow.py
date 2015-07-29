def myPow(x,n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / myPow(x, -n)
    elif (n % 2) == 1:
        return x*myPow(x, n - 1)
    else:
        return myPow(x*x, n/2)

print(myPow(3,2))