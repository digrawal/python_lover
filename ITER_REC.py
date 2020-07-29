#uing iteration method
"""def factorial(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return  fac
number=int(input("enter the number\n"))
print(factorial(number))
"""

#using Recurssion method

def factorial_recursion(n):
    if n==1:
        return  1
    else:
        return n*factorial_recursion(n-1)