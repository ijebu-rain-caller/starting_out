#Object oriented programming is associated with the use of classes and instances
class Dog():
    """A simple attempt to model a dog"""

    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age 

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulates a dog rolling over in response to a command"""
        print(self.name.title() + " rolled over!")

mks_dog = Dog('Geoffrey',6)

print("My dog's name is " + mks_dog.name.title() + ".")
print("My dog is " + str(mks_dog.age) + " years old.")

#To access attributes of an instance we use 'dot notation' as shown above

#You can call a method from a class by also using the dot notation 
mks_dog.sit()
mks_dog.roll_over()

kazs_dog = Dog('bingo',3)

print("\nMy girlfriend also has a dog, its name is " + kazs_dog.name.title())
print("Its slightly younger than mine at " + str(kazs_dog.age) + " years!")

kazs_dog.sit()
kazs_dog.roll_over()

#TRY IT YOURSELF 
class Restaurant():
    """A simple model for a start-up restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """This describes the type of restaurant"""
        print("This particular restaurant serves " + self.cuisine_type)
        print("It goes by the name " + self.restaurant_name)

    def open_restaurant(self):
        """States the open status of the restaurant"""
        print("This restaurant has officially opened up for business")


mks_restaurant = Restaurant('BalabluSpot','Fish Food')

print("The name of my restaurant is " + mks_restaurant.restaurant_name)
print("My restaurant specializes in " + mks_restaurant.cuisine_type + " cuisine!")

mks_restaurant.describe_restaurant()
mks_restaurant.open_restaurant()

sekis_restaurant = Restaurant("Seki's Bistro",'Burgers')
yemis_restaurant = Restaurant('YOLO coffee','Beverages')

sekis_restaurant.describe_restaurant()
yemis_restaurant.describe_restaurant()




class User():
    """A simple model of a user for a purpose"""
    def __init__(self,first_name,last_name,height,ethnicity):
        """User information"""
        self.first_name = first_name
        self.last_name = last_name 
        self.height = height
        self.ethnicity = ethnicity

    def describe_user(self):
        """Prints a summary of the users information"""
        print("\nAll you need to know about this user: ")
        print("Name: " + self.first_name.title() + ' ' + self.last_name.title())
        print("Height: " + str(self.height) + "cm")
        print("Ethnicity: " + self.ethnicity.title())

    def greet_user(self):
        """This is used to greet the user"""
        print("\nHello " + self.last_name.title() + "!")

user_1 = User('mubarak','sule',136,'yoruba')

user_1.describe_user()
user_1.greet_user()


#When you write a class, you are defining the general behavior that a
#whole category of objects can have 