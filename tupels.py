my_tuple = ("Grapes",8,True,"banana")


print(len(my_tuple))
# print(type(my_tuple))


#If there is only one value in the tuple then you have to add a comma at the end
my_tuple_1 = (8)
# print(type(my_tuple_1))


my_tuple_2 = (8,)

# Tuple also have negetive indexing mechanism
# -1 mean far right element of the tuple


# print(my_tuple[-4])


#If you want to change the value of the tuple you have to convert it to list
my_list = list(my_tuple)
my_list[1] = "apple"

# print(my_list)

#There can be nested tuple as well

my_nested_tuple = ((1,2,3),("apple","banana","grapes"),(True,False))

print(my_nested_tuple[1][1])
print(my_nested_tuple[2][1])
