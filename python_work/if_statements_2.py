#Checking whether a value is in a list
toppings_list = ['anchovies', 'pineapples', 'onions', 'chicken', 'beef']
if 'onions' and 'chicken' in toppings_list:
    print('The pizza available contains onions/chickens')

'onions' in toppings_list

banned_users = ['winner1', 'winner2', 'winner3', 'winner4']
user = 'winner5'

if user not in banned_users:
    print(user.title() + ", is free to register for the courses.")

#Boolean Expressions
game_active = True
can_edit = False 

#Try it yourself
helm = 'green'
if helm == 'green':
    print('Wild')
else:
    print('This sucks')

day_1 = 23
day_2 = 46

if day_1 <=100 and day_2 <=100:
    print('The values lie within the 100 day range')

cake = ['strawberry', 'blueberry', 'red velvet', 'chocolate']
for cak in cake:
    if cak != 'vanilla':
        message = 'All flavors have been checked against the vanilla flavor'
print(message)



rides = ['Ferrari', 'Lambo', 'Audi']
rider = 'Toyota'
if rides != rider:
    print(rider.lower() + ', is not allowed in the car competition!') 

foods = ['beans', 'noodles', 'rice', 'chicken', 'turkey']
for food in foods:
    if food == 'beans':
        print(food.title() + ', the king of all proteins!')


