# you can use mutiple data types in lists

my_list= ["dog","cat","lion",5,True]
print(my_list)
print(my_list[3])
print(type(my_list[4]))

#List have following properties
# * Python list are ordered
# * Python list are changeable

my_list[1]="sam"
print(my_list)

# To view the length of the list we use len()
print(len(my_list))


#Python have negetive indexing mechanism
# -1 mean far right element of the list
print(my_list[-5])

print(my_list[1:4],type(my_list[1:4]))


