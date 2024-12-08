class Car:
    category = 'motor vehicle'


    def __init__(self,name):
        self.name = name

    def display(self):
        print("Name: ",self.name)

    def update_name(self,new_value):
        self.name = new_value


new_car = Car("Audi")

new_car.display()

new_car.update_name("BMW")

new_car.display()