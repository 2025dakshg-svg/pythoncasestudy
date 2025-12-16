# main.py
from wallet import Wallet

wallet = Wallet("Student", 5000)

while True:
    print("\nPerforming Wallet Operation")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Mini Statement")
    print("5. Exit")
   
    choice = input("Enter choice: ")

    if choice == "1":
        wallet.check_balance()

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        wallet.deposit(amount)

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        wallet.withdraw(amount)

    elif choice == "4":
        wallet.mini_statement()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
