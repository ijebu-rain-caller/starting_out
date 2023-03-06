#Slicing a list
players = ['Johnny', 'Rita', 'Sophia', 'Simon']
print(players[0:3])

birds = ['finch', 'crow', 'eagle', 'hummingbird', 'starlight']
print('The two most interesting birds are: \n')
for bird in birds[2:4]:
    print('The ' + bird.title())

print(birds[:3])

print(birds[2:])

#Copying a new list
fave_chows = ['Toast', 'Bread', 'Cauliflower', 'Meat', 'Eggs']
my_chows = fave_chows[:]
print('A list of all my favorite meals are showns below:')
print(my_chows)

fave_chows.append('Turkey')
print(fave_chows)
print(my_chows)

#TRY IT YOURSELF
schools = ['karate', 'judo', 'taekwando', 'jui-jitsu', 'mua thai']
print('The first three items in the list are: ')
print(schools[:3])

print('The three items from the middle of the list are: ')
print(schools[1:4])

print('The last three items in the list are: ')
print(schools[2:])


pizzas = ['pepperoni', 'cheese', 'pineapple', 'steak', 'chicken']
friend_pizzas = pizzas[:]
pizzas.append('ravioli')
friend_pizzas.append('pickle')

print('My favorite pizzas are: ')
print(pizzas)
print("My friend's favorite pizzas are: ")
print(friend_pizzas)

for pizza in pizzas:
    print(pizza)

for fpizza in friend_pizzas:
    print(fpizza)
