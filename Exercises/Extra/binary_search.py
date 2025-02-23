python_list = [1,2,3,4,5,6,7]


def binary_search(numbers_list,number):
    high = len(numbers_list)
    low =0 
    

    while(low<high):
        mid_point = low + (high-low)//2
        print("Hello")
        value = numbers_list[mid_point]
        if value==number:
            return True
        elif value<number:
            low = mid_point+1
        else:
            high = mid_point

    
    return False

binary_search(python_list,8)



# for value in range(1,8):
#     result = binary_search(python_list,value)
#     print(result)