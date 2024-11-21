user_input = input("Enter a number: ")
num = int(user_input)

squred_list = []
increment = 1
count = 1

while increment <= num:
    squred_list.append(increment)
    count += 1
    increment = count * count

print(squred_list)