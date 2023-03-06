#Using a while loop with Lists and Dictionaries 
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for user in confirmed_users:
    print(user.title())

#Removing all instances of specific values from a list 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#Filling a dictionary with User Input
responses = {}

polling_active = True 

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which food would you like to eat someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name + " would like to eat " + response + " someday!")


#TRY IT YOURSELF
sandwich_orders = ['peanut butter','pastrami', 'fish', 'pastrami', 'ham','pastrami']
finished_sandwiches = []

print("Kindly note that the deli has run of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print("Your " + sandwich.title() + " sandwich is ready!")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwhiches have been made: ")
for fin in finished_sandwiches:
    print(fin.title())

#Dream Vacation Poll
user_response = {}

active = True

while active:
    details = input("\nKindly input your name: ")
    dream_vacay = input("\nWhere is your dream vacation spot? ")
    user_response[details] = dream_vacay

    finito = input("\nType in yay or nay to enable the next user: ")
    if finito.lower() == 'nay':
        active = False

print("\nResults of the dream vacation poll: ")
for user,response in user_response.items():
    print(user.title() + " would like to visit " + response.title())




