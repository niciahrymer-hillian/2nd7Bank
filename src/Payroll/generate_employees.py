import random
import csv

print("Starting generation...")

# Lists of first names and last names for generating random names
first_names = ["John", "Jane", "Bob", "Alice", "Charlie", "Diana", "Edward", "Fiona", "George", "Helen", "Ian", "Julia", "Kevin", "Linda", "Michael", "Nancy", "Oliver", "Patricia", "Quinn", "Rachel", "Sally", "Tom", "Ursula", "Victor", "Wendy", "Xavier", "Yvonne", "Zach"]
last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes"]

def generate_employee():
    name = random.choice(first_names) + " " + random.choice(last_names)
    hours = random.randint(20, 80)
    rate = round(random.uniform(10.0, 50.0), 2)
    return [name, hours, rate]

print("Opening file...")
with open('/Users/nicky/Projects/2nd7Bank/src/Payroll/input.data', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Hours-worked', 'Hourly-rate'])
    for i in range(500000):
        if i % 100000 == 0:
            print(f"Generated {i} employees")
        writer.writerow(generate_employee())

print("Done!")