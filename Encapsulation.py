class Car:
    def __init__(self,brand,model,_internal_number,__private_number):
        self.brand = brand
        self.model = model
        self._internal_number = _internal_number
        self.__private_number = __private_number
    def get_private_number(self):
        return self.__private_number

my_car = Car("BMW","I5","TN009","FGDY997")

print(my_car.brand) # Accessing public attributes is fine no problem
print(my_car.model) # Accessing public attributes is fine no problem

print(my_car._internal_number) #This will run but not recommended(_this is for internal use only usually with in the class or its subclass)

# print(my_car.__private_number) # This will raise an AttributeError
print(my_car.get_private_number())

'''
BMW
I5
TN009
FGDY997
'''
