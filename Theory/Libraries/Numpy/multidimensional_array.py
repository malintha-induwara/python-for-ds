import numpy as np


array_1 = np.array([[1,2,3],[4,5,6]])

array_2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

#print(array_1)
#print(type(array_1))

#shape
print(array_1.shape)
print(array_2.shape)

#size
print(array_1.size)
print(array_2.size)

#ndim
print(array_1.ndim)
print(array_2.ndim)

#dtype
print(array_1.dtype)
print(array_2.dtype)
