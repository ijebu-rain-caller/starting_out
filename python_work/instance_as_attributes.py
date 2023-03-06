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
        
        

class Battery():
    """A simple attempt to model an electric car's battery."""
    def __init__(self,battery_size=70):
        """Initializes the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Checks the battery size and upgrades when necessary."""
        if self.battery_size != 85:
            self.battery_size = 85
            print("Battery capacity has been appropriately set!")
        elif self.battery_size == 85:
            print("Battery capacity is already set to 85.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initializes the appropriate attributes"""
        super().__init__(make, model, year)
        self.battery = Battery()

my_electric_benz = ElectricCar('Benz','C',2016)
my_electric_benz.battery.describe_battery()
my_electric_benz.battery.get_range()

#TRY IT YOURSELF
my_electric_benz.battery.upgrade_battery()
my_electric_benz.battery.get_range()

