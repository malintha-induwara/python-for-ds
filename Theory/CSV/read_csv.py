import csv

csv_file = 'customers-100.csv'


with open(csv_file,'r',newline='') as csv_file_data:
    csv_reader = csv.reader(csv_file_data)

    for row in csv_reader:
        print(row,type(row))
   
print(csv_reader)
print(type(csv_reader))
