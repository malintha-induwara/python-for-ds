#Writing files to a json file

import json

data = {
        "name": "Sam",
        "age": 30,
        "city":"LA"
        }



json_file = 'new_json.json'

with open(json_file,'w') as new_json:
   
    #Serialize the dict to a JSON formated string ( it take a input a dict and output a json string)
    #Indent use to define the 4 spaces from start

    json_data = json.dumps(data,indent=4)
    new_json.write(json_data)
    new_json.write("\n")
7
