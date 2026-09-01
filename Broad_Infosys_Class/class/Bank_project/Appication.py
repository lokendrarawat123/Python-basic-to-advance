from Function import findAccountbyAccountNumber
from Bank import Bank
from Storage import accounts
from ErrorHandle import DepositAmountError,WithdrawAmountError,AccountNotFoundError

def bankApp():
    while True:
        print('Welcome to Bank Application')
        print('1. Create Account')
        print('2. Deposit Amount')
        print('3. Withdraw Amount')
        print('4. User Details')
        print('5. Exit')

        choice=int(input('Enter your choice: '))
        if choice==1:
            y_n=input('Do you really want to create account(yes/no): ')
            if y_n=='yes':
                print('Create Account')
                
                print('-'*30)
                name=input('Enter account holder name: ')
                balance=int(input('Enter your initial balance: '))
                job=input('Enter your job position: ')
                if balance>100:
                    b=Bank(name,balance,job)
                    accounts.append(b)
                    print(f'Account created with name {name} deposit balance is {balance} with account number {b.account_number}')
                else:
                    print('Insufficient deposit balance.Balance must be more than Rs.100')
            else:
                print('Continue with your transaction')
            
        elif choice==2:
            y_n=input('Do you want to deposit amount(yes/no)')
            if y_n=='yes':
                print('Deposit Amount')
                print('-'*30)
                acc_number=input('Enter your account number: ')
                try:
                    
                    find_acc=findAccountbyAccountNumber(acc_number)
                    if find_acc:
                        amount=int(input('Enter your deposit amount'))
                        find_acc.depositeAmount(amount)
                except AccountNotFoundError as anfe:
                    print(anfe)
                except DepositAmountError as dae:
                    print(dae)
            else:
                print('Continue with your transaction')
                
                
        elif choice==3:
            y_n=input('Do you want to withdraw amount(yes/no)')
            if y_n=='yes':
                print('Withdraw Amount')
                print('-'*30)
                acc_number=input('Enter your account number: ')
                try:
                    find_acc=findAccountbyAccountNumber(acc_number)
                    if find_acc:
                        amount=int(input('Enter Your withdraw amount'))
                        find_acc.withdrwaAmount(amount)
                except AccountNotFoundError as anfe:
                    print(anfe)
                except WithdrawAmountError as wae:
                    print(wae)
            else:
                print('Continue with your transaction')
        elif choice==4:
            y_n=input('Do you want to see Your details(yes/no)')
            if y_n=='yes':
                print('User Details')
                acc_number=input('Enter your account number: ')
                try:
                    find_acc=findAccountbyAccountNumber(acc_number)
                    if find_acc:
                        find_acc.userDetails()
                except AccountNotFoundError as afe:
                    print(afe) 
            else:
                print('Continue with your transaction')
        elif choice==5:
            print('Thank you for choosing us')
            break
        else:
            print('Invalid choice.Please choose valid choice')
            
        