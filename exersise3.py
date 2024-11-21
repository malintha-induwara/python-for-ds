my_list = [1,2,3]

length = len(my_list)

match length:
    case 1:
        print("Only one element")
    case 2:
        print("Two elements")
    case 3:
        print("Three elements")
    case _:
        print("Somehitng Else")