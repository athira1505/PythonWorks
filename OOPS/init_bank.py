

# bank[ac_no,balance,ac_type,customer_name]
# req methods:  [initialize,deposit(amount),withdraw(amount),get_bal()]

class Bank():
    ac_no:int
    balance:int
    ac_type=str
    cust_name=str

    def __init__(self,ac_no,balance,ac_type,cust_name):
        self.ac_no=ac_no
        self.balance=balance
        self.ac_type=ac_type
        self.cust_name=cust_name

    def deposit(self,amount):
        self.balance+=amount
        print(f"your{self.ac_no} has been credited with amount {amount} avl bal {self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"your{self.ac_no} has been debited with amount {amount} avl bal {self.balance}")
        else:
            print("insufficient balance")

    def get_bal(self):
        print("your avl balance",self.balance)

customer_instance1=Bank(10000,2500,"savings","asseed")
customer_instance1.withdraw(500)