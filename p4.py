# 4. Function with Default Arguments
# Write a function to calculate simple interest.
# Keep rate default as 5%.

p = int(input("Enter Principle amount 1:"))
i = int(input("Enter Interest 2:"))

def sp(p,i,r=5):
    return p*i*r/100

print("Amount is:",sp(p,i))