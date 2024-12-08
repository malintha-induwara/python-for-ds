# print the some of the digit using recursion

value = 547

def sum_of_digits(value):
    if value == 0:
        return value
    return value%10 + sum_of_digits(value//10)

print(sum_of_digits(value))