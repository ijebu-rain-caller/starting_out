dogs = ['shepherd', 'caucasian', 'poodle', 'collie']
for dog in dogs:
    if dog == 'poodle':
        print('We do not have the poodle for sale')
    else:
         print('The ' + dog.title() + ' dog is for sale!')

if dogs:
    print('We have a variety of dog breeds available!')
else: print('Sorry, we are all out of dogs for the season')

#WOrking with two lists
available_dogs = ['german shepherd', 'boerboel', 'caucasian', 'poodle']

requested_dogs = ['tibetan mastiff', 'boerboel', 'poodle']

for requested_dog in requested_dogs:
    if requested_dog in available_dogs:
        print('The dog breed selected is available!')
    else: 
        print('Sorry, we do not have the ' + requested_dog.title())
print('Kindly proceed to checkout for payment')


#TRY IT YOURSELF 
user_names = ['admin', 'tom', 'jerry', 'timmy', 'violet', 'rudd']
for user in user_names:
    if user == 'admin':
        print('Welcome admin, would you like to see a status report?')
    else: print('Hello ' + user.title() + ' ,thank you for logging in again!')


user_names = []
if user_names:
    print('The usernames are available')
else: 
    print('We need to find some users!')

current_users = ['kunle', 'seun','mubarak', 'sekinat', 'omotomilola']

new_users = ['kunle', 'seun', 'adedeji', 'kelvin', 'melvin']

for new in new_users:
    if new in current_users:
        print('Sorry, this username is unavailable')
    else: print('The username entered is valid')


ord_numbers = [1,2,3,4,5,6,7,8,9]
for numbers in ord_numbers:
    if numbers == 1:
        print(str(numbers) + 'st')
    elif numbers == 2:
        print(str(numbers) + 'nd')
    elif numbers == 3:
        print(str(numbers) + 'rd')
    elif numbers in ord_numbers:
        print(str(numbers) + 'th')


