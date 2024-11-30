
def arbitary_keywords_arguments(**kwargs):
    print(type(kwargs))
    print(kwargs)

    
    for key,value in kwargs.items():
        print(key,value)
    
arbitary_keywords_arguments(number1=23,number2=32,number3=12,name="Hello")