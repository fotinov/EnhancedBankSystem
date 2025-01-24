# Enhanced Bank Account Management System

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
            transaction_histories[index] += transaction
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
            transaction_histories[index] += transaction
            print(f'Withdrawal successful. New balance: ${balances[index]:.2f}')
        else:
            print('Insufficient balance. Please enter a valid amount.')
    else:
        print('Account not found. Please check the name and try again.')

#
def check_balance():
    """Check balance of an account."""
    pass  # TODO: Add logic

def list_accounts():
    """List all account holders and details."""
    pass  # TODO: Add logic

def transfer_funds():
    """Transfer funds between two accounts."""
    pass  # TODO: Add logic

def view_transaction_history():
    """View transactions for an account."""
    pass  # TODO: Add logic

def apply_for_loan():
    """Allow user to apply for a loan."""
    pass  # TODO: Add logic

def repay_loan():
    """Allow user to repay a loan."""
    pass  # TODO: Add logic

def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic

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
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()