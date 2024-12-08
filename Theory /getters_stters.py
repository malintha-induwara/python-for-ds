class Car:
    def __init__(self):
        self.__name = "None"

    def get_value(self):
        return self.__name
    
    def set_value(self,name):
        self.__name = name


new_car = Car()

print(new_car.set_value("BMW"))
print(new_car.get_value())



