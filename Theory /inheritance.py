

# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def make_sound():
#         pass


# class Dog(Animal):

#     def make_sound(self):
#         print(self.name, "says Woow")


# new_dog = Dog("Black")

# new_dog.make_sound()



class Animal:
    def __init__(self,name):
        self.name = name


class Dog(Animal):
    def __init__(self, name,color):
        super().__init__(name)       #Super is a keyword you can do self.name = name but its better to clal super().__init__name()
        self.color = color
        # Animal.__init__(self,name)  #Another way to call the parent class constructor

    def display(self):
        print("Name: ",self.name)
        print("Color: ",self.color)



new_dog = Dog("max","black")
print(new_dog.name, new_dog.color)