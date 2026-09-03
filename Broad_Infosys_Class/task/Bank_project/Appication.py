from Function import findAccountbyAccountNumber, userChoice, staffChoice, SignUp_Login_Choose, findUser
from Bank import Bank
from Storage import accounts
from ErrorHandle import DepositAmountError, WithdrawAmountError, AccountNotFoundError


def userMenu(user):
    while True:
        choice = userChoice()
        if choice == 1:
            y_n = input('Do you want to deposit amount(yes/no): ')
            if y_n == 'yes':
                print('Deposit Amount')
                print('-' * 30)
                try:
                    amount = int(input('Enter your deposit amount: '))
                    user.depositeAmount(amount)
                    print(f'Rs.{amount} deposited successfully. New balance: Rs.{user.initial_balance}')
                except DepositAmountError as dae:
                    print(dae)
            else:
                print('Continue with your transaction')

        elif choice == 2:
            y_n = input('Do you want to withdraw amount(yes/no): ')
            if y_n == 'yes':
                print('Withdraw Amount')
                print('-' * 30)
                try:
                    amount = int(input('Enter your withdraw amount: '))
                    user.withdrwaAmount(amount)
                except WithdrawAmountError as wae:
                    print(wae)
            else:
                print('Continue with your transaction')

        elif choice == 3:
            user.userDetails()

        elif choice == 4:
            print('Logged out successfully.')
            break
        else:
            print('Invalid choice. Please choose valid choice.')


def staffMenu(staff):
    while True:
        choice = staffChoice()
        if choice == 1:
            print('\nAll User Accounts')
            print('=' * 30)
            user_accounts = [acc for acc in accounts if acc.role == 'user']
            if user_accounts:
                for acc in user_accounts:
                    print(f'Name: {acc.name} | A/C No: {acc.account_number} | Balance: Rs.{acc.initial_balance}')
            else:
                print('No user accounts found.')

        elif choice == 2:
            print('Create User Account')
            print('-' * 30)
            name = input('Enter account holder name: ')
            username = input('Enter username: ')
            password = input('Enter password: ')
            job = input('Enter job position: ')
            try:
                balance = int(input('Enter initial balance: '))
                if balance > 100:
                    b = Bank(name, username, password, job, balance, role='user')
                    accounts.append(b)
                    print(f'Account created successfully. A/C No: {b.account_number}')
                else:
                    print('Insufficient deposit balance. Balance must be more than Rs.100')
            except ValueError:
                print('Invalid balance amount.')

        elif choice == 3:
            print('Create Staff Account')
            print('-' * 30)
            name = input('Enter staff name: ')
            username = input('Enter username: ')
            password = input('Enter password: ')
            job = input('Enter job position: ')
            b = Bank(name, username, password, job, role='staff')
            accounts.append(b)
            print(f'Staff account created successfully for {name}.')

        elif choice == 4:
            print('Logged out successfully.')
            break
        else:
            print('Invalid choice. Please choose valid choice.')


def bankApp():
    while True:
        log_in_OR_signup = SignUp_Login_Choose()

        if log_in_OR_signup == 1:
            print('\nSignUp')
            print('-' * 30)
            name = input('Enter your full name: ')
            username = input('Enter username: ')
            password = input('Enter password: ')
            job = input('Enter job position: ')
            try:
                balance = int(input('Enter initial balance: '))
                if balance > 100:
                    b = Bank(name, username, password, job, balance, role='user')
                    accounts.append(b)
                    print(f'Account created successfully! A/C No: {b.account_number}')
                else:
                    print('Insufficient deposit balance. Balance must be more than Rs.100')
            except ValueError:
                print('Invalid balance amount.')

        elif log_in_OR_signup == 2:
            print('\nLogin')
            print('-' * 30)
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            try:
                user = findUser(username, password)
                print(f'\nLogin successful. Welcome, {user.name}!')
                print('-' * 30)
                if user.role == 'staff':
                    staffMenu(user)
                else:
                    userMenu(user)
            except AccountNotFoundError as e:
                print(e)

        elif log_in_OR_signup == 3:
            print('Thank you for choosing us. Goodbye!')
            break
        else:
            print('Invalid choice. Please choose valid choice.')
