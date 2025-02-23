class Car:

    category = 'motor vehicle'

    #if you writing something a class you must use self keyowrd even if there is no parameters
    def display(self):  
        print("This is a car")

    def getCategory(self):
        return self.category

    def setCategory(self,category):
        self.category= category




new_car =Car()


print(new_car.getCategory())

new_car.setCategory("No a motor vehicle")

print(new_car.getCategory())

# You can access class atributes as well using class name
print(Car.category)


#We use construcor to initialize value to the instance


#Class atributes are shared between objects, but intance attributes are only for that specific instance


class Tree:
    def __init__(self,name):    #category is a instance attributes
        self.category = name



new_tree = Tree("Hello")

print(new_tree.category)