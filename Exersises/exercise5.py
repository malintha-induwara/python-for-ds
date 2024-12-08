user_input = input("Enter a number: ")

num = int(user_input)

squred_list = []

for number in range(1,num+1):
    squred_list.append(number*number)

print(squred_list)