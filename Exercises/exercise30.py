#crate a 2d numpy array  with the shape 4 by 5 containing numbers 1 to 20 
#perform the following operations on the matrix
#1. add 10 to all the elements
#2. multply all the elements by 2
#3. calculate the square of all the elements

import numpy as np

array_1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])

print(array_1.shape)
print(array_1)

addition_result = array_1 + 10

multiplication_result = array_1 * 2

square_result = array_1 ** 2

print(addition_result)
print(multiplication_result)
print(square_result)
