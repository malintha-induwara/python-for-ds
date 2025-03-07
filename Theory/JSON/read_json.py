import json

#Path of the file

json_file_path ="example_1.json"


#Open the JSON file
with open(json_file_path,'r') as json_file:
    data = json.load(json_file)


for key,value in data.items():
    print("Key:"+key + " : "+"Value: "+value)
    

print(type(data))
print(data)
