
# This is a One way to do it

# import my_calculator.addition
# import my_calculator.subtract


# result1 = my_calculator.addition.add(5,4)
# result2 = my_calculator.subtract.sub(5,4)


# print("Addition result", result1)
# print("Subtract result", result2)


#########################################

# This is the second way to do it


# from my_calculator import addition
# from my_calculator import subtract

# result1 = addition.add(23,23)
# result2 = subtract.sub(50,20)


# print("Addition result: ",result1)
# print("Subtraction result: ",result2)


#########################################

# This is the thired way to do it


# from my_calculator.addition import add
# from my_calculator.subtract import substract


# result1 = add(30,20)
# result2 = sub(30,20)


# print("Addition result:",result1)
# print("Subtraction result:",result2)



from my_calculator import add,sub

result1 = add(5,3)
result2 = sub(6,2)

print("Addition: ", result1)
print("Substraction: ", result2)
