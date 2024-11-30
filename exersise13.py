#write a python program that take a list of tuples where each tuple contains a 'name' and 'age' and a intiger 
# 1)Use a lambda function to filter out the tuples where the age is less than 18
#  

people = [('Alice', 20), ('Jhon', 17), ('Andrew', 25), ('Kate', 15)]

result = list(filter(lambda item: item[1]>=18 , people))

print(result)