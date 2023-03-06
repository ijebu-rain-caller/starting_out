message = input("Who do you love the most: ")
print(message)

name = input("Kindly enter your name: ")
print("Hello " + name.title() + ", welcome to our world!")

#Building a multi-line string 
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
print(age)

#NB: int() function treats a string as an integer so python understands user input

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride")
else:
    print("You need to be taller to mount this ride")


#TRY IT YOURSELF EXCERCISE 
# % represents the modulo operator and it returns the remainder of a division 
number = input("Type in a number and I'll guess if its even or odd: ")
number = int(number)
if number % 2 == 0:
    print("The number " + str(number) + " is an even one!")
else: print("The number " + str(number) + " is an odd one!")

desired_rental = input("What type of rental car would you like? ")
print("Let me see if I can find you a " + desired_rental.title())

dinner_number = input("How many people are available in your dinner group? ")
dinner_number = int(dinner_number)
if dinner_number > 8 :
    print("Your guests would have to wait for a table")
else:
    print("A table for your guests is ready!")


number = input("I can guess if your number is a multiple of 10: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " is a multiple of 10!")
else:
    print(str(number) + " is not a multiple of 10")

