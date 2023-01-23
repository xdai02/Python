class BankAccount:
    __ACCOUNT_DIGITS = 16
    __owner = ""
    __account = ""
    __balance = 0

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

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False
        self.__balance -= amount
        return True

def main():
    account = BankAccount()
    account.set_owner("Terry")
    account.set_account("6250941006528599")
    account.set_balance(50)

    print("Owner:", account.get_owner())
    print("Account:", account.get_account())
    print("Balance:", account.get_balance())

    account.deposit(100)
    print("Balance:", account.get_balance())

    account.withdraw(70)
    print("Balance:", account.get_balance())

if __name__ == "__main__":
    main()