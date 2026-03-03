balance = 0

def display_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Amount Deposited Successfully")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn Successfully")
    else:
        print("Insufficient Balance")

while True:
    print("\n--- BANK MENU ---")
    print("1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")