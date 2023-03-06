#Passing an arbitrary number of arguments 
def make_egg_roll(*ingredients):
    """Prints all the ingredients used in the particular egg roll"""
    print("\nThe following ingredients were added to this eggroll: ")
    for ingredient in ingredients:
        print("- " + ingredient.title())

make_egg_roll('egg')
make_egg_roll('flour','ata rodo','sprinkles')

#The asterisk creates an empty tuple to store inputs from the function call

def make_pizza(size,*toppings):
    """Specifying the size and topping properties of a pizza"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping.title())

make_pizza(12,'pepperoni','cheese','steak','chicken')

def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for user,info in user_info.items():
        profile[user] = info
    return profile

build_profile('sule','mubarak',age=21,ethnicity='yoruba')

print(build_profile)

def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for user,info in user_info.items():
        profile[user] = info
    return profile

build_profile('sule','mubarak',age='21',ethnicity='yoruba')

print(build_profile)


#TRY IT YOURSELF 

def sand_wich(*ingredients):
    """Making the perfect sand-wich"""
    print("This is a summary of the ingredients in the sandwich: ")
    for tastes in ingredients:
        print("- " + tastes.title())

sand_wich('butter', 'bread', 'ketchup', 'mayo')

def build_profile(first,last,**mk_info):
    """Tells you all about mubarak the funny guy"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in mk_info.items():
        profile[key] = value
    return profile

build_profile('sule','mubarak',age=21,ethnicity='badass')
print(build_profile)


def car_info(manufacturer_name,model_name,**other_info):
    """Stores information about a car type including model etc"""
    car_profile = {}
    car_profile['manufacturer_name'] = manufacturer_name
    car_profile['model_name'] = model_name
    for key,value in other_info.items():
        car_profile[key] = value
    return car_profile

car = car_info('toyota','2017',color='black',opfeature='bulletproof')
print(car)


