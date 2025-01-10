
# Banking Program

def Show_Balance():
    print(f"Your balance is {balance:.2f}")

def Deposit():
    pass

def Withdraw():
    pass

balance = 0
is_running = True 

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Show_Balance()
    elif choice == 2:
        Deposit()
    elif choice == 3:
        Withdraw()
    elif choice == 4:
        is_running = False
    else:
        print("Invalid choice")

print("Thank you have a nice day!")