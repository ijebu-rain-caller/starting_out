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




mks_new_car = Car('benz','ml',2009)
print(mks_new_car.get_descriptive_name())
mks_new_car.read_odometer()
# Modifying an attribute's value for an instance directly
mks_new_car.odometer_reading = 23
mks_new_car.read_odometer()

# Writing a method that updates an attribute's value for you 
mks_new_car.update_odometer(23)
mks_new_car.read_odometer()

#Adding logic to ensure that value cannot be rolled back on 
mks_new_car.update_odometer(5)

#Incrementing an attribute's value through a method
mks_new_car.increment_odometer(7)
mks_new_car.read_odometer()


#TRY IT YOURSELF
class Restaurant():
    """A simple model for a start-up restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """This describes the type of restaurant"""
        print("This particular restaurant serves " + self.cuisine_type)
        print("It goes by the name " + self.restaurant_name)

    def open_restaurant(self):
        """States the open status of the restaurant"""
        print("This restaurant has officially opened up for business")

    def set_number_served(self,number):
        """Sets the number of customers that have been served"""
        self.number_served = number

    def increment_number_served(self,increment):
        """Lets you increment the number of customers who've been served"""
        self.number_served += increment







restaurant = Restaurant('HotDiggity','Hot Dogs')
print("My restaurant has served up to " + str(restaurant.number_served) + " people!")

restaurant.set_number_served(23)
print(restaurant.number_served)

restaurant.increment_number_served(7)
print(restaurant.number_served)


#TRY IT YOURSELF
class User():
    """A simple model of a user for a purpose"""
    def __init__(self,first_name,last_name,height,ethnicity):
        """User information"""
        self.first_name = first_name
        self.last_name = last_name 
        self.height = height
        self.ethnicity = ethnicity
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the users information"""
        print("\nAll you need to know about this user: ")
        print("Name: " + self.first_name.title() + ' ' + self.last_name.title())
        print("Height: " + str(self.height) + "cm")
        print("Ethnicity: " + self.ethnicity.title())

    def greet_user(self):
        """This is used to greet the user"""
        print("\nHello " + self.last_name.title() + "!")

    def increment_login_attempts(self,increment=1):
        """Increments the value of login attempt by 1"""
        self.login_attempts += increment

    def reset_login_attempts(self):
        """This resets the value of login_attempts to 0"""
        self.login_attempts = 0

mk_user = User('sule','mubarak',184,'yoruba')
mk_user.increment_login_attempts()
mk_user.increment_login_attempts()
mk_user.increment_login_attempts()
print(mk_user.login_attempts)
mk_user.reset_login_attempts()
print(mk_user.login_attempts)






