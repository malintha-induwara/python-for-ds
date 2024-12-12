#create a decorator check_positive that
# 1) if the input to a function is a positive number
# 2) if the input is not positive print a message "Input must be a positive number"
# 3) Use this decortor on a function calculate_squre_root that calculate
#     1) take one number as a inpput
#     2) calculate the squre root of the number using math.sqrt

import math

def check_positive(func):
    def wrapper(num):
        if num > 0:
            return func(num)
        else:
            print("Input must be a positive number")
    return wrapper

@check_positive
def calculate_squre_root(num):
    return math.sqrt(num)

print(calculate_squre_root(9))
