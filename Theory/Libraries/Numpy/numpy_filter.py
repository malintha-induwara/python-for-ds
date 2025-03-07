import numpy as np

array = np.array([10,20,30,40,50])

#condition = array > 25
#print(condition)
#result_array = array[condition]

#result_array = array [ array>25]

result_array = array[ (array>20) & (array<50)]



print(result_array)
