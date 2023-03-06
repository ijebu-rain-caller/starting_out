#The below elif function can be used multiple times to test a single given
#test or provided condition
age = 20
if age == 20:
    print("You're 20?, no one has to know baby girl!")
else: 
    print("You wouldn't get the joke ugh!")

age = 17 
if age < 4:
    print("Admission fee is free for this rider!")
elif age < 18: 
    print("Admission fee is $5")
else: 
    print("Admission fee is $10")

#Testing multiple conditionss
list = ['blue', 'green', 'yellow', 'red', 'cyan']
if 'blue' in list:
    print('The color blue is available!')
if 'red' in list:
    print("The color red is available!")

print("These are the colors available")


week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'fridays']
if 'monday' in week_days:
    print('The first day of the work week is recorded!')
elif 'monday' not in week_days:
    print('Incomplete work week!')
if 'tuesday' and 'thursday' in week_days:
    print('The t days are also recorded!')


#TRY IT YOURSELF 
alien_color = 'red'
if 'green' in alien_color:
    print('You have just earned 5 points!')

alien_color = 'green'
if 'green' in alien_color:
    print('You have just earned 5 points!')


alieno_color = 'yellow'
if 'green' in alieno_color:
    print('You just earned 5 points!')
else: 
    print('You just earned 10 points!')


alien = 'red'
if 'green' in alien:
    print('You have just earned 5 points!')
elif 'yellow' in alien:
    print('You have just earned 10 points!')
elif 'red' in alien:
    print('You have just earned 15 points!')


age_mk = 21 
if age_mk < 2:
    print('Mubarak is still a ween!')
elif age_mk >= 2 and age_mk < 4:
    print('Mubarak is still a toddler.')
elif age_mk >= 4 and age_mk < 13:
    print('Mubarak is still a kid.')
elif age_mk >= 13 and age_mk < 20:
    print('Mubarak is a teenake boy!')
elif age_mk >= 20 and age_mk < 65:
    print('Mubarak is an adult man')
elif age_mk >= 65:
    print('Mubarak is an old ass geezer!')


