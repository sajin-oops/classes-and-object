class Car:
    def __init__(self,brand,model,number_plate):
        self.brand = brand
        self.model = model
        self.number_plate = number_plate
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Number_Plate: {self.number_plate}")
    def accelerate(self):
        print("The car is accelerating.")

# Here im going to create a child class
class ElectricCar(Car):
    def __init__(self,brand,model,number_plate,battery_life_kwh):
        super().__init__(brand,model,number_plate)
        self.battery_life_kwh = battery_life_kwh
    def charge(self):
        print(f"The {self.brand} {self.model} is now charging.")
    def accelerate(self):
        print(f"The electric car is accelerating silently.")

#create an object for the parent class
my_car = Car("Bugatti","Bugatti Chiron","TN0972")
my_car.display_info()
my_car.accelerate()
'''
O/P 
Brand: Bugatti, Model: Bugatti Chiron, Number_Plate: TN0972
The car is accelerating.
'''

#Create an object for the child class
my_electric_car = ElectricCar("Tesla","Model 6","NY6700","88")
my_electric_car.display_info()
my_electric_car.charge()
my_electric_car.accelerate()
'''
Brand: Tesla, Model: Model 6, Number_Plate: NY6700
The Tesla Model 6 is now charging.
The electric car is accelerating silently.

'''