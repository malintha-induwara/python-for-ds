#If you want to store key value pair then you can use dictionary


my_dict = {
    "name":"John",
    "price": 100,
    "weight": 50,
    "marks":[80,85,90]
}

my_dict["name"] = "Sam"
my_dict["color"] = "red"

print(my_dict)
print(type(my_dict))

print(my_dict["marks"][0])