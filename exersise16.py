#Calculate the sum of all the elemts in an array or list using recursion

# def sum_of_elements(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + sum_of_elements(arr[1:])







# print(sum_of_elements(my_list)) 




my_list = [1,2,3,4,5,6,7,8,9,10]

def sum_of_elements(arr):
    if len(arr) == 0:  
        return 0
    else:
        return arr.pop(0) + sum_of_elements(arr)
    

print(sum_of_elements(my_list))