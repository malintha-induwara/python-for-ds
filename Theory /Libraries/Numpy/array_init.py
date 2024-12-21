import numpy as np

#Zeros
print(np.zeros(5))
print(np.zeros((2,3),dtype=int))


#Full

print(np.full(8,10))

print(np.full((3,4),7))

#Empty
#It assign garbage values (Usually do this because this is much faster)
print(np.empty((2,3)))
