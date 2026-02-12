# 6. Banking System Using Functions
# Functions for:
# Deposit
# Withdraw
# Check Balance



balance=0
def Deposite(amount):
    global balance
    balance = balance+amount
    return amount
def Withdraw(amount):
    global balance
    balance = balance-amount
    return amount
def Check_balance():
    global balance
    return balance

while True:
    print("1. Depoite")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exite")


    choice=int(input("enter choice number:"))


    match choice:

        case 1:
            amount=int(input("Enter ammount"))
            print("Deposited the amount",Deposite(amount))
        case 2:
            amount=int(input("Enter ammount"))
            if(amount > balance):
                print("Insufficient balance")
            else:
                print("Withdraw amount is:",Withdraw(amount))
        case 3:
             print("Current balance is:",Check_balance())
        case 4:
            exit()

