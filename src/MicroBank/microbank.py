# read the input data from the file
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read().splitlines()
    return data
input_data = read_data('input.data')

# process the data to calculate the balance
def calculate_balance(data: list):
    balance = 0.0
    # each line looks like: 1/10/2026, deposit, 100.00
    for line in data:
        line = line.strip().split(',')
        if line[1].strip().lower() == 'deposit':
            amount = float(line[2].strip())
            balance += amount
        elif line[1].strip().lower() == 'withdrawal':
            amount = float(line[2].strip())
            balance -= amount
    return balance

balance = calculate_balance(input_data)
# print the final balance
print(f"Final Balance: ${balance:.2f}")