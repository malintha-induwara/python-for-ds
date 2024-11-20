#If you want to store key value pair then you can use dictionary


my_dict = {
    "name":"John",
    "price": 100,
    "weight": 50,
    "marks":[80,85,90]
}

my_dict["name"] = "Sam"

#Add new value to the dictionary
my_dict["color"] = "red"

print(my_dict.keys())
print(my_dict)
print(type(my_dict))

#Another wag to get the value from the dictionary
print(my_dict.get("name"))
print(my_dict["marks"][0])


#If you want to remove a key value pair from the dictionary
my_dict.pop("color")

del my_dict["weight"]



#If you want to distory the dictionary
# del my_dict


#If you want to get the value of the key if the key is not present in the dictionary
# print(my_dict.get('expire_date',"2024.02.05"))

# #Update multiple values at the same time
# my_dict.update({"price":200,"color":"red"})

#If you want to remove all the key value pair from the dictionary
my_dict.clear()


print(my_dict)