person = {
    "name" : "jhon",
    "age" : 24,
    "gender": "male"
}


for key,value in person.items():
    print("Key is ",key , "Value is ",value)


for key in person.keys():
    print("Key is ",key)

for value in person.values():
    print("Value is",value)