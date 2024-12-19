#1.create a 1d numpy array with values 1 to 20 use boolean indexing to extract all Even numbers
#2.given the numpy array with elements 10,20,30,40,50, use boolean indexing to extract all elements greater than the mean of the array

import numpy as np

array_1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

even_numbers = array_1[array_1 % 2 == 0]

print(even_numbers)


array_2 = np.array([10,20,30,40,50])

mean = np.mean(array_2)

greater_than_mean = array_2[array_2 > mean]

print(greater_than_mean)

