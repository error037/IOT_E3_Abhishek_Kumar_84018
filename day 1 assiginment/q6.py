def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int (input("input a no. to compute the factorial: "))
print(factorial(n))