#Absoulte Value (mapanka)

print(abs(-5)) 



#Map Function

def squre(x):
    return x*x

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers2 = [10,20,30,40,50,60,70,80,90,100]

result = list(map(squre, numbers))

result_map = map(squre, numbers)

for i in result_map:
    print(i)


print(result)


map_result = list(map(squre, numbers2))
print(map_result)


#write  a code to add the corresponding elements of two lists



my_list_1 = [10,8,5,6]
my_list_2 = [4,3,6,1]

def add(x,y):
    return x+y

result = list(map(add, my_list_1, my_list_2))

print(result)


#Filter Function


my_list = [5,8,10,9,6,3]

def check_even(x):
    return x%2 ==0

results =  filter(check_even,my_list)

converted_results = list(results)

print(results,type(results))
print(converted_results)
