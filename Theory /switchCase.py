response_code = 200

match response_code:
    case 200:
        print("Ok")
    case 201:
        print("Created")
    case 204:
        print("No content")
    case 401:
        print("Forbidden")
    case 403:
        print("Unautherized")
    case 500:
        print("Internal Server Error")
    case _:
        print("Not match")


#match is not extactly match the value it just match the pattern


numbers = [1,2,3]

match numbers:
    case [x,y]:
        print(x*y)
    case [x,y,z]:
        print(x+y)
    case [x,y,z,g,e]:
        print(x+y)
    case _:
        print("Nothing")