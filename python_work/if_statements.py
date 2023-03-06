cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
         print(car.title())

#Conditional Tests
#Python sees if statements as either true or false, if true it executes,
#If false it ignores and moves on to the next line.

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('The order requested for has been mismatched')


answer = []
if answer != 'Sungba':
    print('The actual first release from Asake was Sungba!')

# AND/OR statements can be used in IF statements as conditional checks 
number_1 = 35
number_2 = 33
if number_1 >= 20 and number_2 <= 40:
    print('The number stored is below 40')

age_0 = 21
age_1 = 42 
if age_0 >= 21 or age_1 <= 42:
    print('The age bracket lies between 21 and 42')


#TRUE OR FALSE COMMANDS 
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

cars = 'lexus'
print(cars != 'lexus')

age_1 = 32
age_2 = 21
print(age_1 > 10 and age_2 < 50)