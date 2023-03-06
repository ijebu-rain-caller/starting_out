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

class IceCreamStand(Restaurant):
    """A simple model of an Ice cream stand."""
    def __init__(self,flavors,restaurant_name,cuisine_type):
        """Initializes the flavors that the ice cream stand has to offer."""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Displays the flavors available with the ice cream stand"""
        print("The flavors available in the ice-cream stand are: ")
        for flavor in self.flavors:
            print(flavor.title())

flave = ['vanilla','chocolate','banana']
my_ice_cream = IceCreamStand(flave,'mks','ice-cream')
my_ice_cream.display_flavors()


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


list_0 = ['can add post','can delete post','can ban user']
class Privileges():
    """Stores a list of strings on admin privileges"""
    def __init__(self,privileges=list_0):
        """Initializes the privileges for the admin user."""
        self.privileges = privileges

    def show_privileges(self):
            """Shows the privileges an admin is entitled to."""
            print("The administrator's set of privileged are: ")
            for privilege in self.privileges:
                print(privilege.title())


class Admin(User):
        """Initialize administrator privileges."""
        def __init__(self,first_name,last_name,height,ethnicity):
            """User information"""
            super().__init__(first_name,last_name,height,ethnicity)
            self.privileges = Privileges()


mk_admin = Admin('Mubarak','Sule',140,'Yoruba')
mk_admin.privileges.show_privileges()







