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


#If you want to create a new list from exsisting list
print(my_list[1:4],type(my_list[1:4]))


#If you get values from the begining you dont have to mention 0
print(my_list[:3],type(my_list[:3]))


#same as above if you get value to the end
print(my_list[2:],type(my_list[2:]))  #This is equal to print(my_list[2:5],type(my_list[2:5]))


#Change list items
random_list = [10,5,"Cat","Dog",True]

#Insert a value to a specific index
random_list.insert(2,"Rat")
print(random_list,len(random_list))

#Append a value to the end of the list
random_list.append("Elephant")
print(random_list,len(random_list))

#Combined two list to one
my_list.extend(random_list)
print(my_list,len(my_list))


#remove value form end of the list

my_list.pop(2)
print(my_list,len(my_list))

#Another way to remove value


del my_list[2]

my_list.clear()
# del my_list

print(my_list,len(my_list))


