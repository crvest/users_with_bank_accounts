class BankAccount:
    all_accounts = []
    def __init__(self, account_balance = 0, interest_rate = 0.01):
        self.account_balance = account_balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)   # logs each instance of an account created to array all_accounts
    
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance *= 1 + self.interest_rate
            return self
    
    # prints all instances of account balance
    @classmethod
    def display_accounts(cls):
        for account in cls.all_accounts:
            print(account.account_balance)


# # create 2 accounts
# wolverine = BankAccount()
# spiderman = BankAccount()

# # wolverine makes 3 deposits, 1 withdrawl, yield interest and display account info
# wolverine.deposit(100).deposit(200).deposit(450).withdraw(300).yield_interest().display_account_info()

# print("------------")

# # spiderman make 2 deposits, 4 withdrawls, yields interest, and display account info
# spiderman.deposit(500).deposit(1000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

# print("------------")

# # NINJA BONUS
# BankAccount.display_accounts()