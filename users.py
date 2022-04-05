from bankaccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(account_balance = 0, interest_rate = 0.02) 

    def make_deposit(self, amount):
        self.account.account_balance += amount
    
    def make_withdrawl(self, amount):
        self.account.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.account_balance}")
    
    def transfer_money(self, other, amount):
        self.make_withdrawl(amount)
        other.make_withdrawl(amount)

# create 3 users
tom = User("Tom", "tom@tom.tom")
bill = User("Bill", "bill@bill.bill")
spiderman = User("Peter", "p.parker@friend.ly")

#  tom makes 3 deposits, 1 withdrawl, and displays balance
tom.make_deposit(300)
tom.make_deposit(100)
tom.make_deposit(100)
tom.make_withdrawl(250)
tom.display_user_balance()

print("----------------")

# bill makes 2 deposits and 2 withdrawls and displays balance
bill.make_deposit(50)
bill.make_deposit(50)
bill.make_withdrawl(25)
bill.make_withdrawl(75)
bill.display_user_balance()

print("----------------")

# spiderman makes 1 deposit and 3 withdrawls and displays balance
spiderman.make_deposit(1000)
spiderman.make_withdrawl(400)
spiderman.make_withdrawl(200)
spiderman.make_withdrawl(50)
spiderman.display_user_balance()

print("----------------")

# bonus: tom transfers money to spiderman, prints both balances
tom.transfer_money(spiderman, 100)
tom.display_user_balance()
spiderman.display_user_balance()