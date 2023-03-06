alien_0 = {'color': 'blue', 'point': 5}
print(alien_0['color'])
# A dictionary in python is a collection of key-value pairs

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

newd = {}
newd['name'] = 'mubarak'
newd['age'] = 21
newd['state'] = 'Ogun State'
print(newd)

#Key-value pairs essentially make up dictionaries in python 
mental_health = {'status': 'ok', 'timeline': '1yr'}
print('Lately, my mental health has been ' + mental_health['status'] + '!')

mental_health['status'] = 'not ok'
print('Unfortunately, my mental health is ' + mental_health['status'] + ' anymore')

#Tracking the position of an alien character with a certain speed
alien_0 = {'x_position': 0, 'y_position': 20, 'speed': 'medium'}
print("Original Position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 5
elif alien_0['speed'] == 'medium':
    x_increment = 10
else:
    x_increment = 20

alien_0['x_position'] = alien_0['x_position'] + x_increment


print("New x-position: " + str(alien_0['x_position']) )

benzene = {'goat': 1, 'ram': 2, 'sheep': 3}
del benzene['goat']
print(benzene)

classes = {
    'emeka':'highway',
    'paschal':'structures',
    'awolusi':'analysis',
    }

print('The most enjoyable course is ' + classes['paschal'].title())



