This project is a Python Wallet Management System that allows users to deposit money, withdraw money, check their balance, and view recent transactions. The project uses Object-Oriented Programming, decorators, and file handling, with the code divided into separate files for better structure. A decorator in utils.py ensures that only positive amounts are allowed for deposit and withdrawal, while the Wallet class in wallet.py handles all wallet operations and logs each transaction with date and time in a text file. Below is the core implementation used in the project:
# utils.py
def require_positive(func):
    def wrapper(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return False
        return func(self, amount)
    return wrapper
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

    @require_positive
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
            return
        self.balance -= amount
        self.log_transaction(amount, "Withdrew")

    def mini_statement(self):
        with open("transactions.txt", "r") as file:
            for line in file.readlines()[-5:]:
                print(line.strip())
