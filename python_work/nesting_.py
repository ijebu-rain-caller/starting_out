monkey_1 = {'color': 'brown','points': 5}
monkey_2 = {'color': 'cream', 'points': 10}
monkey_3 = {'color': 'white', 'points': 15}

monkeys = [monkey_1, monkey_2, monkey_3]

for monkey in monkeys:
    print(monkey)

#Generating a fleet of 30 aliens
monkeys = []
for monkey_number in range(30):
    new_monkey = {'color': 'green', 'points': 5, 'speed': 'slow'}
    monkeys.append(new_monkey)

#To show only 5 of the monkey stored
for mon in monkeys[:5]:
    print(mon)

#To show how many monkeys have been created
print("Total number of monkeys: " + str(len(monkeys)))

#Changing the properties of the first three monkeys stored 
for monkey in monkeys[:3]:
    if monkey['color'] == 'green':
        monkey['color'] = 'beige'
        monkey['speed'] = 'medium'
        monkey['points'] = 16
    print(monkey)

#Inputing a list in a dictionary 
pizza = {'crust':'plain', 'toppings': ['pepperoni','cheese']}
print("You ordered a " + pizza['crust'] + " pizza crust" +
" with the following toppings:\n")

for topping in pizza['toppings']:
    print(topping)

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['R'],
    'edward': ['ruby','go'],
    'phil': ['python', 'c++']
}


for name,value in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for val in value:
        print("\t" + val.title())


users = {
    'winner': 
    {'first':'Sunday',
    'last':'James',
    'location':'Ekiti'
    },
    'mubarak': 
    {'first':'Abayomi',
    'last':'Sule',
    'location':'Lagos'
    },
    
    }

for username,user_info in users.items():
    print("\nUsername: " + username.title())
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

