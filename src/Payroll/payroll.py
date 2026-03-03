import csv

def read_data(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data

input_data = read_data('input.data')

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

payroll = calculate_payroll(input_data)

def print_payroll(payroll):
    print(f"{'Name':<20} {'Total Pay':<15} {'Taxes':<10} {'Net Pay':<10}")
    for name, total_pay, taxes, net_pay in payroll:
        print(f"{name:<20} {total_pay:<15.2f} {taxes:<10.2f} {net_pay:<10.2f}")

print_payroll(payroll)

def write_output(file_name, payroll):
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Name', 'Total Pay', 'Taxes', 'Net Pay'])
        for name, total_pay, taxes, net_pay in payroll:
            csv_writer.writerow([name, f"{total_pay:.2f}", f"{taxes:.2f}", f"{net_pay:.2f}"])

# write_output('output.data', payroll)