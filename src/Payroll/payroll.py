import csv
import os

def read_data(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data
    # data is a list of lists, where each inner list represents a row from the CSV file

def append_data(file_name, records):
    file_exists = os.path.exists(file_name)
    file_empty = not file_exists or os.path.getsize(file_name) == 0
    with open(file_name, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        if file_empty:
            csv_writer.writerow(['Name', 'Hours', 'Rate'])
        csv_writer.writerows(records)


def interactive_input():
    records = []
    while True:
        employee_name = input("Enter employee name: ")
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))
        records.append([employee_name, hours_worked, hourly_rate])

        another = input("Add another entry? (y/n): ").strip().lower()
        if another != 'y':
            break

    return records


def main():
    while True:
        print("1. Read data from file")
        print("2. Enter data interactively")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            input_data = read_data('input.data')
            payroll = calculate_payroll(input_data)
            print_payroll(payroll)
            # write_output('output.data', payroll)  # Uncomment to write output to file
        elif choice == '2':
            employee_data = interactive_input()
            append_data('input.data', employee_data)
            input_data = read_data('input.data')
            payroll = calculate_payroll(input_data)
            print_payroll(payroll)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")
    

def calculate_payroll(data):
    payroll = []
    for row in data[1:]:  # Skip header
        name, hours_worked, hourly_rate = row
        hours_worked = float(hours_worked)
        hourly_rate = float(hourly_rate)
        total_pay = hours_worked * hourly_rate
        taxes = total_pay * 0.2  # Assuming a flat tax rate of 20%
        net_pay = total_pay - taxes
        payroll.append((name, total_pay, taxes, net_pay))
    return payroll

def input_data(self, employee_name, hours_worked, hourly_rate):
        self.employee_name = employee_name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        return self.employee_name, self.hours_worked, self.hourly_rate

def print_payroll(payroll):
    print(f"{'Name':<20} {'Total Pay':<15} {'Taxes':<10} {'Net Pay':<10}")
    for name, total_pay, taxes, net_pay in payroll:
        print(f"{name:<20} {total_pay:<15.2f} {taxes:<10.2f} {net_pay:<10.2f}")

def write_output(file_name, payroll):
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name', 'Total Pay', 'Taxes', 'Net Pay'])
        for name, total_pay, taxes, net_pay in payroll:
            csv_writer.writerow([name, f"{total_pay:.2f}", f"{taxes:.2f}", f"{net_pay:.2f}"])
         

# run the payroll processing
if __name__ == "__main__":
    main()