class BankAccount:
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

def main():
    account = BankAccount()
    account.owner = "Terry"
    account.account = "6250941006528599"
    account.balance = 50

    print("Owner:", account.owner)
    print("Account:", account.account)
    print("Balance:", account.balance)

    account.deposit(100)
    print("Balance:", account.balance)

    account.withdraw(70)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()