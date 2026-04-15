#importing data from date and time to record transactions with timestamps
import datetime
# read the input data from the file
DATA_FILE = 'input.data'

# read the input data from the file

def read_data(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()
# pulling the data from the input data file

def calculate_balance(data: list):
    balance = 0.0
# calculating the balance by iterating through the transactions in the data list    
    for line in data:
        parts = line.strip().split(',')  # Split the line into parts based on comma
        if len(parts) < 3: # Ensures the format is valid or it will ckip/continue to the next line if it is not
            continue
        transaction_type = parts[1].strip().lower() # Get the transaction type and convert it to lowercase for consistency
        amount = float(parts[2].strip())
        if transaction_type == 'deposit':
            balance += amount
        elif transaction_type == 'withdrawal':
            balance -= amount
    return balance

# Append a new transaction to the file with the current date, transaction type, and amount
def append_transaction(file_name, transaction_type, amount):
    now = datetime.datetime.now()
    date_text = f"{now.month}/{now.day}/{now.year}"
    with open(file_name, 'a') as file:
        file.write(f"{date_text}, {transaction_type}, {amount:.2f}\n")


def main():
    while True:
        print('\nWelcome to MicroBank!')
        print('Withdrawal')
        print('Deposit')
        print('Check Balance')
        print('Exit')
        choice = input('Choose an option to start your transaction: ').strip().lower()

        if choice == 'withdrawal':
            input_data = read_data(DATA_FILE) # Read the current transactions from the file to calculate the current balance
            balance = calculate_balance(input_data) # Calculate the current balance based on the transactions read from the file
            print(f'Current Balance: ${balance:.2f}') # Display the current balance to the user before they enter the withdrawal amount
            amount = float(input('Enter amount to withdraw: ')) # Prompt the user to enter the amount they wish to withdraw and convert it to a float for calculation
            if amount > balance:
                print('Insufficient funds.')
            else:
                append_transaction(DATA_FILE, 'withdrawal', amount) # Append the withdrawal transaction to the file with the current date, transaction type, and amount
                balance -= amount
                print(f'Withdrawal successful. New Balance: ${balance:.2f}') # Display the new balance to the user after the withdrawal transaction has been processed

        elif choice == 'deposit':
            input_data = read_data(DATA_FILE)# Read the current transactions from the file to calculate the current balance before the deposit
            balance = calculate_balance(input_data)# Calculate the current balance based on the transactions read from the file before the deposit
            print(f'Current Balance: ${balance:.2f}')# Display the current balance to the user before they enter the deposit amount
            amount = float(input('Enter amount to deposit: '))# Prompt the user to enter the amount they wish to deposit and convert it to a float for calculation
            append_transaction(DATA_FILE, 'deposit', amount)# Append the deposit transaction to the file with the current date, transaction type, and amount
            balance += amount
            print(f'Deposit successful. New Balance: ${balance:.2f}')# Display the new balance to the user after the deposit transaction has been processed

        elif choice == 'check balance':
            input_data = read_data(DATA_FILE) # Read the current transactions from the file to calculate the current balance when the user chooses to check their balance
            balance = calculate_balance(input_data) # Calculate the current balance based on the transactions read from the file when the user chooses to check their balance
            print(f'Current Balance: ${balance:.2f}')# Display the current balance to the user when they choose to check their balance

        elif choice == 'exit':
            print('Thank you for using MicroBank. Goodbye!')
            break

        else:
            print('Please choose a valid option.')

# The main function serves as the entry point of the program, providing a menu for the user to interact with the banking system. It allows users to perform withdrawals, deposits, check their balance, or exit the program. The program continuously prompts the user until they choose to exit, ensuring a seamless banking experience.
if __name__ == '__main__':
    main()