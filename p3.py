# 3. Function to Calculate Factorial (Using Recursion)
# Implement factorial using:
# Normal function
# Recursive function

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
