# 2. Function to Find Largest of Three Numbers
#  Accept three numbers as parameters.
#  Return the largest number.
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
           return num1
    elif(num2>num1):
        if(num2>num3):
           return num2
    else:
        return num3


print("Biggest number is:",max(num1,num2,num3))