#you are task with creating a python program to manage a companies employee record stored in csv file
# the program should read the employee details from a csv file filter the records based on the condition
# and wirte the filtered records to a new csv file to a new csv file
# 1) input file "employees.csv" contains the following fields EmployeeID,Name,Department,Salary
# Sample data
# 1,John,IT,60000
# 2,Jane,HR,55000
# 3,Mike,Finance,70000
# 4,Linda,IT,65000

# Output file name: high_salary_employee.csv you will create this file
# It should contain records of employees whos salaries are above 60000
# The fields should remain the same
# 1) Read the input file (use csv.reader to read employees.csv and display all the records)
# 2) Filter the records based on the condition (salary > 60000)
# 3) Write the filterd records use csv.DictWriter to write the records to the new file high_salary_employee.csv

import csv

def read_csv_file():
    with open("employees.csv","r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

def filter_records():
    with open("employees.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        high_salary_employees = []
        for row in csv_reader:
            if int(row['Salary']) > 60000:
                high_salary_employees.append(row)
        return high_salary_employees
    
def write_csv_file(high_salary_employees):
    with open("high_salary_employee.csv", "w", newline="") as csv_file:
        field_names = ["EmployeeID", "Name", "Department", "Salary"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        csv_writer.writeheader()
        for row in high_salary_employees:
            csv_writer.writerow(row)

read_csv_file()
high_salary_employees = filter_records()
write_csv_file(high_salary_employees)
