#write a function called employee_info that accept a required 'name' parameter and arbitrary number of keyword arguments reprecenting addintioal details about the employee. The function should
# 1) print the name of the employee
# 2) iteriate though the keywords arguments and print each key-value pair in the format "<key>:<value>" 
# 3) modify the employee info function to return a dictionay containing all the employee details (including the name and additional attributes passed via kwargs)


def employee_info(name,**kwargs):
    print(name)
    for key,value in kwargs.items():
        print(key,":",value)

    employee_info = {'name':name }
    employee_info.update(kwargs)
    

    return employee_info

employee_info("Sam",age=20,role='developer',salary=2000)

print(employee_info("Sam",age=20,role='developer',salary=2000))