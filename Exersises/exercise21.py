class MyClass:
    def __init__(self):
        self.__data = "Some data"

    def __check_my_values(self):
        print("Checking values")

    def check_values(self):  
        self.__check_my_values()


new_instance = MyClass()
new_instance.check_values()


