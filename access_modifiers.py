class MyClass:
    def __init__(self):
        self.var_1 = "Public value"
        self._var_2 = "Protected value"
        self.__var_3 = "Private attribute"

    def _protected_method(self):
        print("Protected Method")

    def __private_method(self):
        print("Private Method")

new_instance = MyClass()


print(new_instance.var_1)
print(new_instance._var_2)

# You cant access private attribute from outside of the class
# print(new_instance.__var_3)


# You can do this but it is discouraged
new_instance._protected_method()   

# You cant access private method from outside
# new_instance.__private_method()

