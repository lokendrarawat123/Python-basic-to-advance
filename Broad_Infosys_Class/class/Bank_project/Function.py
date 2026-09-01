from ErrorHandle import AccountNotFoundError
from Storage import accounts
def findAccountbyAccountNumber(acc_number):
    for account in accounts:
        if account.account_number==acc_number:
            return account
    else:
        raise AccountNotFoundError('Account Number Error: Account not found with given account number does not found.')