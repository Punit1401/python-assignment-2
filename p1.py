# 1. Write a Function to Perform Arithmetic Operations
#  Create separate functions for addition,
# subtraction, multiplication, and division.
#  Call them based on user input.

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

choice=int(input("Enter arethimitc operation:"))

match choice:
    case 1:
        print("Total:",add(num1,num2))
    case 2:
       print("Total:",sub(num1,num2))
    case 3:
       print("Total:",mul(num1,num2))
    case 4:
       print("Total:",div(num1,num2))


