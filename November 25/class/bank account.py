class Bank_Account:
    def __init__(self,acc_no,name,acc_type,):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=0
        print("Hello !!! Welcome to the Deposit & Withdraw Bank")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited:"))
        self.balance+=amount
        print("Amount Deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn:"))
