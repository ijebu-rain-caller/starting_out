#Positional Arguments
def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','cornelius')
describe_pet('cat','okotomeow')

#Keyword arguments(involves the use of key-value pairs)
def describe_house(owner,house_type):
    """Displays info on the house owner and house type"""
    print("\nThe owner of the house is " + owner.title())
    print("It is a " + house_type.title() + " building")

describe_house(owner='otedola', house_type='facade')

#Default values are stored in the function's definition
#TRY IT YOURSELF 
def make_shirt(shirt_message, shirt_size = 'Large'):
    """Shirt details for a customer"""
    print("\nThe size of the shirt ordered is " + shirt_size + ".")
    print("Shirt message: " + shirt_message.title())

make_shirt(shirt_message= "I love python")
make_shirt(shirt_message= "I love python", shirt_size= "Medium")
make_shirt(shirt_message= "the experience", shirt_size= "XXXL")

def describe_city(name,country='Nigeria'):
    """This function accepts the name of a city and its country"""
    print(name.title() + " is in " + country.title())

describe_city(name='Ibadan')
describe_city('Lagos')
describe_city(name='France',country='Paris')

#Returning a value
def get_formatted_name(first_name,last_name):
    """Returns the full name of a user's input"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#THE LINE DIRECTLY BELOW IS CALLED A FUNCTION CALL 
get_formatted_name('sule','mubarak')
mks_name = get_formatted_name('sule','mubarak')
print(mks_name)

#Making an argument optional 
def new_formatted_name(first_name,last_name,middle_name=""):
    """It returns the full name of the user with the option of exluding middle"""
    if middle_name:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
    else: 
        full_name = first_name + ' ' + last_name
    return full_name.title()

user_deetz = new_formatted_name('sule','mubarak')
print(user_deetz)

user_deetz = new_formatted_name('sule','mubarak','adedeji')
print(user_deetz)

#Returning a dictionary 
def build_person(first_name,last_name):
    """A function that stores information about an individual"""
    person = {'first':first_name,'last':last_name}
    return person

things_about_him = build_person('sule','mubzz')
print(things_about_him)


def build_new_person(first_name,last_name,age=""):
    """Just watch and see"""
    person ={'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person 

new_guy = build_new_person('sule','abayomi',23)
print(new_guy)

#Using functions alongside data strcutures like while loops 
def get_formatted_name(first_name,last_name):
    """Returns the full name of a user's input"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

credit = True
while credit:
    print("\nPlease tell me your name: ")
    print("Enter 'stop' at any time to quit")
    f_name = input("First name: ")
    if f_name.lower() == 'stop':
        break
    l_name = input("Last name: ")
    if l_name.lower() == 'stop':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name.title() + "!")
    

#FINAL TRY IT YOURSELF
def city_country(city_name,city_country):
    """Takes in the name of a city and its country."""
    city_deetz = city_name.title() + ", " + city_country.title()
    return city_deetz

my_city_choice = city_country('santiago','chile')
print(my_city_choice)
my_city_choice = city_country('sao paulo','brasil')
print(my_city_choice)
my_city_choice = city_country('ibadan','nigeria')
print(my_city_choice)


def make_album(artist_name,album_title,music_genre,no_of_tracks=""):
    """This function tells us all about a particular music album"""
    artist_e = {'name':artist_name,'title':album_title,'genre':music_genre}
    if no_of_tracks:
        artist_e['tracks'] = no_of_tracks
    return artist_e

finale_e = make_album('tyler,the creator', 'IGOR', 'rap',no_of_tracks=10)
print(finale_e)
finale_e = make_album('rema','rave & roses', 'afro-beat')
print(finale_e)


def make_album(artist_name,album_title):
    """This function tells us all about a particular music album"""
    artist_e = {'name':artist_name,'title':album_title,}
    return artist_e

while True:
    print("Enter the artist's name and album title ")
    print("(Enter in 'q' to end the program)")
    a_name = input('Artist name: ')
    if a_name == 'q':
        break 
    a_title = input('Album title: ')
    if a_title == 'q':
        break 
    album_deetz = make_album(a_name.title(),a_title.title())
    print(album_deetz)

