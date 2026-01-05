#Task 1: Calculate Factorial Using a Function

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

num=int(input("Enter a number: "))
print(f"Factorial of {num} is:",factorial(num))