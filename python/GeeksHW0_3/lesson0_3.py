class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        self.password = password
        self.balance = balance

    def get_balance(self):
        return self.balance
    
ardager = BankAccount("ardager","12234","1111")

print(ardager.balance)