for value in range(1,5):
    print(value)
#Range funct. helps us specify a bunch of numbers in python
#list() helps us create a list of the range specified in this example
numbers = list(range(1,21))
print(numbers)
for number in numbers:
    print("This is the " + str(number))

#We might desire to skip certain numbers in a list, here's how: For a bunch
#of odd numbers between 1 and 12.
odd_numbers = list(range(1,12,2))
print(odd_numbers)

#** represents exponents in python code, write a code for squares from 1-10
square_numbers = []
for stuff in range(1,11):
    square = stuff**2
    square_numbers.append(square)

print(square_numbers)


#TRY IT YOURSELF SECTION    
digits = range(1,420)
zino = sum(digits)
lee = min(digits)
skyy = max(digits)
print(str(zino) + "  " + str(lee) + "  " + str(skyy))
#When concatenating always specify str() on numerical values

#List comprehensions allows you to generate lists in shorter code
square_numbers = [value**2 for value in range(1,11)]
print(square_numbers)


not_so = []
for value in range(1,21):
    not_so.append(value)

print(not_so)

new_list = []
one_million = list(range(1,1000001))
for value in one_million:
    new_list.append(value)

print(new_list)


one_million = list(range(1,1000001))
min(one_million)
max(one_million)
wonka = sum(one_million)
print(wonka)

odd = []
odd_future = list(range(1,21,2))
for newodd in odd_future:
    odd.append(newodd)

print(odd)

cubes = []
first_ten = list(range(1,11))
for first in first_ten:
    cubo = first**3
    cubes.append(cubo)

print(cubes)

first_ten = [first**3 for first in range(1,11)]
print(first_ten)







