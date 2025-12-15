# 2
class BankHisobi:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"Balance: {self.balance}, owner: {self.owner}"


Ali = BankHisobi("Ali", 100)
print(Ali)
Ali.deposit(100)
print(Ali)
Ali.withdraw(40)
print(Ali)
