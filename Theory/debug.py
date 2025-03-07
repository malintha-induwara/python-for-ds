# import pdb

def multiplication(a,b):
    answer = a * b
    return answer


# pdb.set_trace()

#From python 3.7 onward you can use  breakpoint for debugging
breakpoint()

x = input("Enter first number : ")
y = input('Enter second number :')

mul = multiplication(x,y)

print(mul)