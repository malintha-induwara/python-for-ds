
# Decorators
# 
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner


# tem_var = outer(10)

# print(type(tem_var))
# print(tem_var(5))



# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()

#     return inner



# def ordinary():
#     print("I am ordinary")



# decoreated_fun = make_pretty(ordinary)
# decoreated_fun()


# This way of defining decorators also equal to above

def make_pretty(func):
    def inner():
        print("I Got Decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()