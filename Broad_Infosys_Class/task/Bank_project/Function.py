from ErrorHandle import AccountNotFoundError
from Storage import accounts


def findAccountbyAccountNumber(acc_number):
    for account in accounts:
        if account.account_number == acc_number:
            return account
    raise AccountNotFoundError('Account Number Error: Account not found with given account number.')


def findUser(username, password):
    for account in accounts:
        if account.username == username and account.password == password:
            return account
    raise AccountNotFoundError('Login Error: Invalid username or password.')


def SignUp_Login_Choose():
    print('\nWelcome to Bank Application')
    print('1. SignUp')
    print('2. Login')
    print('3. Exit')
    try:
        user_input = int(input('Enter your choice: '))
        return user_input
    except ValueError:
        print('Invalid input. Please enter a number.')
        return -1


def userChoice():
    print('\n--- User Menu ---')
    print('1. Deposit Amount')
    print('2. Withdraw Amount')
    print('3. My Details')
    print('4. Logout')
    try:
        choice = int(input('Enter your choice: '))
        return choice
    except ValueError:
        print('Invalid input. Please enter a number.')
        return -1


def staffChoice():
    print('\n--- Staff Menu ---')
    print('1. View All Accounts')
    print('2. Create User Account')
    print('3. Create Staff Account')
    print('4. Logout')
    try:
        choice = int(input('Enter your choice: '))
        return choice
    except ValueError:
        print('Invalid input. Please enter a number.')
        return -1
