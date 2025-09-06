class Account:
    def __init__(self,balance,account_no):
        self.bal=balance
        self.acc=account_no

    def debit(self,amount):
        self.bal=-amount
        print ("RS",amount,"was debited")
        print("Current Balance:", self.get_balance())

    def credit(self,amount):
        self.bal=+amount
        print ("RS",amount,"was credited")
        print("Current Balance:", self.get_balance())

    def get_balance(self):
        return self.bal            

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
print(acc1.acc)