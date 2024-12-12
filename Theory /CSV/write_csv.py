#Writing CSV File

import csv 

csv_file = 'sample_data.csv'



data = [
    {"Name":"Jhone doe","Age":30,"City": "New York"},
    {"Name":"Jane Simith","Age":28,"City": "Los Angles"},
    {"Name":"Bob Johnson","Age":30,"City": "Chicago"}
]



field_names = ["Name","Age","City"]


with open(csv_file,'w',newline='') as file:
   csv_writer = csv.DictWriter(file,fieldnames = field_names)
   csv_writer.writeheader()

   for row in data:
       csv_writer.writerow(row)
