import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename,'w') as file_object:
    json.dump(username,file_object)
    print("We'll remember you when you come back, " + username + "!")

#The json module can be used to store data when a program is closed
# json.dump() is used to store while json.load() is used to access


#Refactoring - process of breaking your code into a series of functions that 
#have specific jobs.


def get_stored_username():
    """Retrieve a stored username if there's any"""
    filename = 'username.json'
    try:
        with open(filename) as f_o:
            username = json.load(f_o)
    except FileNotFoundError:
        return None
    else:
        return username
    
def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename,'w') as file_object:
            json.dump(username,file_object)
            print("We'll remember you when you come back, " + username + "!")

greet_user()

#CLEAR THIS BLOCK OF CODE BEFORE RUNNING THIS FILE 
import json

with open('username.json') as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")


filename = 'bizabiza.json'

try:
    with open(filename) as file_object:
        lets_go = json.load(file_object)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back " + lets_go + "!")



    

