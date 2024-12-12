#protected properties and methods are not really protected in Python. 
# They are just a convention to tell other developers that they should not access those properties or methods.

class Animal:
    def __init__(self):
        self.data = "Some data"

    def _make_sound(self):
        print("Making sound")

class Dog(Animal):

    def bark(self):
        self._make_sound()
        print("Woof")


new_dog = Dog()

new_dog.bark()
print(new_dog.data)
new_dog._make_sound()
