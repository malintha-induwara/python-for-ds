#you are given a json file name student.json which contains the information about students and their grades in json list
#your task is to 
#1. read the file 
#2. display the name of all students who scored above 75
#3. add a new student record to the file
#4. save the updated data back to the json file


import json

def read_json_file():
    with open("student.json","r") as json_file:
        data = json.load(json_file)
        return data
    
def students_above_75(data):
    for student in data:
        if student["grade"] > 75:
            print(student["name"])

def add_student(data):
    name = input("Enter name: ")
    grade = int(input("Enter grade: "))
    
    new_student = {
        "name": name,
        "grade": grade
    }
    
    data.append(new_student)
    
    with open("student.json","w") as json_file:
        json_data= json.dumps(data,indent=4)
        json_file.write(json_data)





data = read_json_file()

students_above_75(data)

add_student(data)

# data = read_json_file()

# print(data)
