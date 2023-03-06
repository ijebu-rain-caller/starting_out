mubaraks_details = {'firstname':'Mubarak', 'lastname':'Sule', 'age':21, 'city':'Lagos'}
print(mubaraks_details['firstname'])
print(mubaraks_details['age'])
print(mubaraks_details['city'])
print(mubaraks_details['lastname'])

glossary = {
    'variable':'A feature that allows you to store a string of characters',
    'list':'Allows you to store a bunch of elements/values',
    'tuple': 'This is an immutable list',
    'string': 'This represents a set of characters',
    'dictionary': 'This contains pieces of related information',
    }

print("Variable: " + glossary['variable']+ "\n")
print("List: " + glossary['list'] + '\n')
print("Tuple: " + glossary['tuple'] + '\n')
print("String: " + glossary['string'] + "\n")
print("Dictionary: " + glossary['dictionary'])


user_0 = {'username':'Udara',
    'first':'Jango',
    'last':'Gogo',
    }

#The items() method picks out both the key and value in a key-value pair
for key,value in user_0.items():
   print("\nKey: " + key)
   print("Value: " + value)

#The keys() method works with just the key in the key-value pair 
for key in user_0.keys():
    print(key.title())

favorite_languages = {'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil','sarah']
for name in favorite_languages.keys():
    if name in friends:
        print("Hi " + name.title() + ", I see your fave language is " + 
        favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our polls!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the polls!')

#To work with just the values, use the values() method
print('The following programming languages have been mentioned:')
for value in favorite_languages.values():
    print(value.title())

#A set is similar to a list except each item in a set must be unique,
#Used to rule out repititions.
print('The following languages have been mentioned:')
for value in set(favorite_languages.values()):
    print(value.title())

   #TRY IT YOURSELF
glossary = {
    'variable':'A feature that allows you to store a string of characters',
    'list':'Allows you to store a bunch of elements/values',
    'tuple': 'This is an immutable list',
    'string': 'This represents a set of characters',
    'dictionary': 'This contains pieces of related information',
    'loop': 'performs an action repeatedly',
    'method': 'performs an action on a list/variable/dictionary',
    'del': 'deletes a value or an item',
    'sorted': 'temporarily sorts a grouped piece of infomation',
    'sort': 'permanently changes the order of a group of info'
    }

for key,value in glossary.items():
    print(key.title() + ': ' + value + '.')

rivers = {'Nile': 'Egypt', 'Niger': 'Chad', 'Elemi': 'Ekiti'}
for river,country in rivers.items():
    print('The ' + river.title() + ' river runs through ' + country.title())


favorite_languages = {'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll_takers = ['winner', 'sarah', 'francis', 'edward', 'adufe']
for poll in poll_takers:
    if poll in favorite_languages.keys():
        print(poll.title() + ', it was nice to have you take the poll!')
    else: print(poll.title() + ', you are invited to take the poll!')


 