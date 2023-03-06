#Inheritance can be used when the new class created is a specialized version
#of another.
#Original - Parent class,New - Child class

class Car():
    """A simple attempt to represent a car."""
    def __init__(self,make,model,year):
        """Initialize attributes to describe a car"""
        self.make = make 
        self.model = model
        self.year = year 
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        proper_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return proper_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car had " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self,mileage):
        """Set the odomoter reading to a given value, reject change
        if anyone tries to roll it back """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """Increment the value of the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """This fills up the car with fuel for commuting"""
        print("The car is now filled with fuel.")


#When one class inherits from another, it automatically takes all
#the attributes and methods from the first class
class ElectricCar(Car):
    """Respresents aspects of a car, specific to electric vehicles"""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class, Then initializes
        attributes of the child class"""
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

#super() helps make a connection between parent and child class

my_electric_car = ElectricCar('Tesla','S',2020)
print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()






