fruits = ['banana', 'apple', 'orange', 'berry', 'pineapple', 'pear', 'pawpaw']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

print('Here is the original list:')
print(fruits)

print('\nHere is the sorted list:')
print(sorted(fruits))
#sorted is temporary, sort is permanent. reverse=True switches the order to reverse


beans = ['white beans', 'black beans', 'red beans', 'whole beans']
beans.reverse()
print(beans)
#Changes the order of the list to reversed 

len(beans)

dream_locations = ['Dubai', 'Canada', 'France', 'London']
print(dream_locations)
print(sorted(dream_locations))

locations = ['Paris', 'Denmark', 'France', 'Sweden', 'Albania', 'Portugal']
print(locations)
print(sorted(locations))

locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)


len(locations)
message = len(locations)
print(message)
print('A total of ' + str(message) + ' are invited to the dinner party!')

#index error means python can't find the index you specified.