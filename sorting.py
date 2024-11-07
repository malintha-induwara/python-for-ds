my_list = ["Grapes","apple","orange","banana"]

#The .sort() method is case sensitive and do sorting alphabatical order
my_list.sort()
print(my_list)


my_value_list = ["Grapes","apple","orange","banana"]

#If you want to sort the List without considering the case sensitivity (case insensitive)

my_value_list.sort(key=str.lower)
print(my_value_list)


#By default list sort assending order if you want to do decending order 

my_value_list.sort(reverse=True)
print(my_value_list)

