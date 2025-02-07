class Bank:
    bank_name = 'SBI'
    def __init__(self,name,age,bal):
        self.name=name
        self.age=age
        self.user_bal = bal

    def get_info(self):
        print(f'''User Name: {self.name} and User Balance: {self.age} and {self.user_bal}''')

b1 = Bank('Pooja',26,55000)
print(b1.bank_name)
print(Bank.bank_name)

b1.get_info()