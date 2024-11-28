def my_func(n):
    return lambda a : a * n

my_double = my_func(2)

print(my_double(4))