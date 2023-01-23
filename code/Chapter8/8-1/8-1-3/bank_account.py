class BankAccount:
    def __init__(self, owner, account, balance):
        self.__ACCOUNT_DIGITS = 16
        
        if owner != "":
            self.__owner = owner
        
        if len(account) == self.__ACCOUNT_DIGITS:
            self.__account = account
        
        if balance >= 0:
            self.__balance = balance
    
    def set_owner(self, owner):
        if owner != "":
            self.__owner = owner
    
    def get_owner(self):
        return self.__owner

    def set_account(self, account):
        if len(account) == self.__ACCOUNT_DIGITS:
            self.__account = account

    def get_account(self):
        return self.__account

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        
        self.__balance += amount
        return True

    def withdraw(self, amount, fee=0):
        if amount <= 0 or amount + fee > self.__balance:
            return False
        
        self.__balance -= amount + fee
        return True

def main():
    account = BankAccount("Terry", "6250941006528599", 50)

    print("Account Balance:", account.get_balance())

    account.withdraw(20)
    print("Account Balance:", account.get_balance())

    account.withdraw(10, 1)
    print("Account Balance:", account.get_balance())

if __name__ == "__main__":
    main()