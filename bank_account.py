class BankAccount:
    """ A Class that defines a bank account """

    def __init__(self, balance, int_rate):
        self.balance = balance
        self.interest_rate = int_rate

    def __str__(self):
        return f"Your account balance: {self.balance:.2f}\nYour interest rate: {self.interest_rate}\n"

    def deposit(self, amount,):
        self.balance += amount
        print(f"You deposited: {amount}\n")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"You deposited: {amount}\n")

    def gain_interest(self):
        interest_gains = (self.balance * self.interest_rate)/100
        self.balance += interest_gains

brody_account = BankAccount(2000, 2.7)
brody_account.gain_interest()
print(brody_account)

brody_account.deposit(320)
brody_account.deposit(4230)
brody_account.deposit(520)
brody_account.deposit(3320)

print(brody_account)

brody_account.withdraw(500)

print(brody_account)

brody_account.gain_interest()

print(brody_account)