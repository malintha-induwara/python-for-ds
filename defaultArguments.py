#we can define default values

def add_numbers(a,b=5):
    return a + b

print(add_numbers(4))


#if you difine default values all the values should be in the far right 
# 
# this is incorrect
# 
# def multiply_numbers (a,c=5,b):
#     return a *b * c

def multiply_numbers (a,b,c=5):
    return a *b * c

print(multiply_numbers(10,20,30))