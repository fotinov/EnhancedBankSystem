# Enhanced Bank Account Management System
#test
# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []         # Account balances
transaction_histories = []  # Account transaction logs
loans = []            # Account loan details
MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")

def create_account():
    """Create a new account."""
    user_name = input('Enter your first and last name: ')  # TODO: Add logic

    user = {
        'name': user_name,
        'balance': 0.00,
        'loan': 0.00,
        'transaction_history': []
    }
    account_holders.append(user['name'])
    balances.append(user['balance'])
    loans.append(user['loan'])
    transaction_histories.append(user['transaction_history'])
    print(f'Account created for {user_name} with initial balance of $0.')


def deposit(account_holders, balances):
    """Deposit money into an account."""
    print("\n--- Deposit Money ---")
    user_name = input('Enter your first and last name: ')
    
    if user_name in account_holders:
        index = account_holders.index(user_name)
        deposit_amount = float(input('Enter the amount to deposit: $'))
        
        if deposit_amount > 0:
            balances[index] += deposit_amount
            transaction = f'Deposit: ${deposit_amount:.2f}'
            transaction_histories[index].append(transaction)
            print(f'Deposit successful. New balance: ${balances[index]:.2f}')
        else:
            print('Invalid deposit amount. Please enter a positive number.')
    else:
        print('Account not found. Please check the name and try again.')

def withdraw():
    """Withdraw money from an account."""
    user_name = input('Enter your first and last name: ') # TODO: Add logic

    if user_name in account_holders:
        index = account_holders.index(user_name)
        withdraw_amount = float(input('Enter the amount to withdraw: $'))

        if withdraw_amount <= balances[index]:
            balances[index] -= withdraw_amount
            transaction = f'Withdrawal: ${withdraw_amount:.2f}'
            transaction_histories[index].append(transaction)
            print(f'Withdrawal successful. New balance: ${balances[index]:.2f}')
        else:
            print('Insufficient balance. Please enter a valid amount.')
    else:
        print('Account not found. Please check the name and try again.')


def check_balance():
    """Check balance of an account."""
    user_name = input('Enter your first and last name: ') # TODO: Add logic

    if user_name in account_holders:
        index = account_holders.index(user_name)
        print(f'Your Balance is: ${balances[index]:.2f}')
    pass  # TODO: Add logic

def list_accounts():
    for account in account_holders:
        print(f'Account Holder: {account}, Loans: ${loans[account_holders.index(account)]}, Balance: ${balances[account_holders.index(account)]:.2f}')

    """List all account holders and details."""
    pass  # TODO: Add logic

def transfer_funds():
    """Transfer funds between two accounts."""
    user_name = input('Enter your first and last name: ')  # TODO: Add logic
    transfer_account = input('Enter the account to transfer funds: ')
    if transfer_account in account_holders:
        index = account_holders.index(user_name)
        transfer_amount = float(input('Enter the amount to transfer: $'))

        if transfer_amount <= balances[index]:
            balances[index] -= transfer_amount
            transfer_index = account_holders.index(transfer_account)
            balances[transfer_index] += transfer_amount
            transaction = f'Transfer: ${transfer_amount:.2f}'
            transaction_histories[index].append(transaction)
            transaction_histories[transfer_index].append(transaction)
            print(f'Transfer successful. New balance for {user_name}: ${balances[index]:.2f}, New balance for {transfer_account}: ${balances[transfer_index]:.2f}')
        else:
            print('Insufficient balance. Please enter a valid amount.')
    pass  # TODO: Add logic

def view_transaction_history():
    user_name = input('Enter your first and last name: ')
    if user_name in account_holders:
        index = account_holders.index(user_name)
        print(f'Transaction History for {user_name}:')
        print(', '.join(transaction_histories[index]))
    """View transactions for an account."""
    pass  # TODO: Add logic

def apply_for_loan():
    user_name = input('Enter your first and last name: ')
    loan_amount = float(input('Enter the amount for the loan: $'))
    if user_name in account_holders:
        index = account_holders.index(user_name)
        if loan_amount <= MAX_LOAN_AMOUNT - loans[index]:
            loans[index] += loan_amount
            interest_amount = loan_amount * INTEREST_RATE
            transaction = f'Loan Application: ${loan_amount:.2f}, Interest: ${interest_amount:.2f}'
            transaction_histories[index].append(transaction)
            balances[index] += loan_amount
            print(f'Loan application successful. New balance: ${balances[index]:.2f}, New loan amount: ${loans[index]:.2f}')
        else:
            print('Loan application failed. Maximum loan amount reached.')
    """Allow user to apply for a loan."""
    pass  # TODO: Add logic

def repay_loan():
    user_name = input('Enter your first and last name: ')
    repay_amount = float(input('Enter the amount to pay: $'))
    if user_name in account_holders:
        index = account_holders.index(user_name)
        if loans[index] >= repay_amount:
            loans[index] -= repay_amount
            interest_amount = repay_amount * INTEREST_RATE
            balances[index] -= interest_amount
            transaction = f'Loan Repayment: ${repay_amount:.2f}, Interest: ${interest_amount:.2f}'
            transaction_histories[index].append(transaction)
            balances[index] -= repay_amount
            print(f'Loan repayment successful. New balance: ${balances[index]:.2f}, New loan amount: ${loans[index]:.2f}')
        else:
            print('Loan repayment failed. Insufficient loan amount.')
    """Allow user to repay a loan."""
    pass  # TODO: Add logic


def identify_card_type():

    card_number = ''.join(filter(str.isdigit, input("Enter your credit card number: ").strip()))

    if card_number.startswith('4'):
        if len(card_number) in {13, 16, 19}:
            if any(card_number.startswith(prefix) for prefix in
                    ('4026', '417500', '4508', '4844', '4913', '4917')):
                return 'Visa Electron'
            return 'Visa'

    if len(card_number) == 15 and card_number.startswith(('34', '37')):
        return 'American Express'

    if len(card_number) == 16:
        if card_number.startswith(('51', '52', '53', '54', '55')) or \
                (222100 <= int(card_number[:6]) <= 272099):
            return 'MasterCard'

    if 16 <= len(card_number) <= 19:
        if card_number.startswith(('6011', '65')) or \
                card_number.startswith(tuple(str(i) for i in range(644, 650))) or \
                (622126 <= int(card_number[:6]) <= 622925):
            return 'Discover'

    if 12 <= len(card_number) <= 19:

        if card_number.startswith(('6759', '676770', '676774')):
            return 'Maestro UK'

        maestro_prefixes = ('5018', '5020', '5038', '5893', '6304',
                            '6759', '6761', '6762', '6763')
        if card_number.startswith(maestro_prefixes):
            return 'Maestro'

    return 'Unknown'

def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit(account_holders, balances)
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print(f"💳 Card Type: {identify_card_type()}")
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()