# += represents an increment/addition on a value or string
#while loops keep running until the condition is false
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 

prompt = "\nTell me something, I'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

#In a situation where multiple events could stop a program, do this
#Flags are used to test in these situations

prompt = "\nTell me something, I'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True 
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nWhat is your favorite movie of all time: "
prompt += "\n(Type 'quit' to exit this prompt) "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
       print(message.title())

#Using the break function in a while loop
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else: 
        print("I'd love to go to " + city.title() + "!")

#Using the continue function in a while loop 
current_number = 0 
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else: print(current_number)

#CTRL - C can be used to exit an infinite loop with infinite results in the terminal



