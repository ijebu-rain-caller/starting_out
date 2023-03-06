houses = ['Cottage', 'Mansion', 'Skyscraper', 'Igloo']

popped_house = houses.pop(2)
#The pop function "pops" off your desired value and stores it in a variable.

print(houses)

del houses[0]
#The del function is used to clear of a value in the list using its index

print(houses)

houses.insert(2, 'Semi-Detached')
#The insert function helps store a new value with an index in the list.

print(houses)

houses.append('Lake house')
#The append function just adds a value after the last in a list.

print(houses)
house_option = "My desired crib is a " + "\n\t" + houses[-2]
#houses[-2] defines the index of the "Semi-detached" value.
print(house_option)

houses.remove('Igloo')
#The remove function is used when the post. isn't known

print("\nA " + houses[0].title() +" is to expensive for me.")

#TRY IT YOURSELF 3-4,3-5,3-6,3-7
celebrities = ['Mac Miller', 'Timothee Chalamet', 'Tyler,The Creator']
message = "I would love to invite you to my dinner party, Mr "
print(message + celebrities[0])
print(message + celebrities[1])
print(message + celebrities[2])

unavailable = "Mr." + celebrities[2] + " would not make the party unfortunately"
print(unavailable)
celebrities.remove('Tyler,The Creator')
celebrities.insert(2,'Damson Idris')
print(celebrities)

print(message + celebrities[0])
print(message + celebrities[1])
print(message + celebrities[2])

print("A bigger table has been found to accommodate new guests")
celebrities.insert(0,'Janet Jackson')
celebrities.insert(2, 'Asake')
celebrities.insert(6, 'Joji')
print(celebrities)


popped_guest1 = celebrities.pop(0)
eyah = "We are deeply sorry to inform you that the capacity won't suffice, Mr. "
print(eyah + popped_guest1)

popped_guest2 = celebrities.pop(1)
print(eyah + popped_guest2 )

popped_guest3 = celebrities.pop(2)
print(eyah + popped_guest3)

popped_guest4 = celebrities.pop(2)
print(eyah + popped_guest4)

print(celebrities)


