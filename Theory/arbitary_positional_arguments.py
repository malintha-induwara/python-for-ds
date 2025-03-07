
#If you dont know the arguments in advanced
def print_args(*args):

    # args is a tuple

    print(args)
    print(type(args))
    print('Positional arguments:', args)

    print("#############################################")

    for arg in args:
        print(arg)



print_args(3, 2, 1, 'wait!', 'uh...')