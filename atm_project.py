balance = 180000

def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"{amount} is successfully deposited!")
        checkbalance()
    else:
        print("Invalid amount")
def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient Balance")
    elif amount <= 0:
        print("Invalid amount")
    else:
        balance -= amount
        print(f"{amount} has been withdrawn successfully!")
        checkbalance()


def checkbalance():
    print(f"Your available balance is: {balance}")



def atm_menu():
    while True:
        print("\n------- ATM Menu ------")
        print("1.deposit")
        print("2.withdraw")
        print("3.checkbalance")
        print("4. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            checkbalance()
        elif choice == "4":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice")

atm_menu()




