import random
from ErrorHandle import DepositAmountError,WithdrawAmountError
class Bank:
    def __init__(self,name,initial_balance,job_position):
        self.name=name
        self.initial_balance=initial_balance
        self.job_position=job_position
        self.account_number=self.name[1:3]+''.join(str(random.randint(0,9)) for i in range(16))+self.job_position[1:3]
    def depositeAmount(self,amount):
        if amount>100:
            self.initial_balance+=amount
        else:
            raise DepositAmountError('Amount Error: Deposit amount must be more than Rs.100')
    def withdrwaAmount(self,amount):
        if amount <self.initial_balance:
            self.initial_balance-=amount
            print(f'Rs.{amount} has been withdrwan from A/C no.{self.account_number}')
        else:
            raise WithdrawAmountError('Amount Error: Withdraw amount must be less than available balance.')
    def userDetails(self):
        print('User Details')
        print('='*30)
        print(f'Account Holder Name:{self.name}')
        print(f'Account Number : {self.account_number}')
        print(f'Balance Amount : Rs.{self.initial_balance}')
        print(f'Job Position : {self.job_position}')