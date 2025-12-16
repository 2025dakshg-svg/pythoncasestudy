# wallet.py
import datetime
import os
from utils import require_positive

class Wallet:
    def __init__(self, owner_name, initial_balance=0):
        self.owner = owner_name
        self.balance = initial_balance

        if not os.path.exists("transactions.txt"):
            open("transactions.txt", "w").close()

    def log_transaction(self, amount, transaction_type):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("transactions.txt", "a") as file:
            file.write(f"{now} - {transaction_type} {amount}\n")

    def check_balance(self):
        print("Current Balance:", self.balance)

    @require_positive
    def deposit(self, amount):
        self.balance += amount
        self.log_transaction(amount, "Deposited")
        print("Transaction Successful: Deposited", amount)

    @require_positive
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
            return False
        self.balance -= amount
        self.log_transaction(amount, "Withdrew")
        print("Transaction Successful: Withdrew", amount)

    def mini_statement(self):
        print("\nMini Statement:")
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
            for line in lines[-5:]:
                print(line.strip())
