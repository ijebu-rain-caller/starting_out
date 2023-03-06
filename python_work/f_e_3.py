# Writing to a file  
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("Programming is a useful endeavor!\n")
    file_object.write("It is a source of problem solving innovations.\n")

#You can open files in various types of modes such as
#read mode('r'), write mode ('w'), append mode ('a'), read and write ('r+')
#Omitting any of these automatically opens the file in read-only mode


with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("The insights I get help me profer efficient solutions!\n")


#TRY IT YOURSELF

new_file = "guest_book.txt"

with open(new_file,'w') as file_object:
        file_object.write('')

guest_name = ''

flag = True
while flag:
    guest_name = input("Kindly input your full name: ")
    message = "\nWelcome to the party, " + guest_name.title()
    if guest_name == "End":
        flag = False
        break
    with open(new_file,'a') as file_object:
          file_object.write(message + '\n')
          file_object.write(guest_name.title() + " has visited our software!")

#When exceptions occur, python tries to manage errors that arise during the
#the program's execution.

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")


#Simple calculator that does only a single division
print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


#Handling the FileNotFoundError Exception 
filename = 'alice.txt'

try:
    with open(filename) as file_object:
         file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)


title = 'We all want something'
message = title.split()
print(message)

#This particular function is able to count the number of words stored in a text file
#It is a form of text analysis
#The code 


def count_words(filename):
    """Count the approximate number of words in a file."""
    try: 
        with open(filename) as file_object:
          contents = file_object.read()
    except FileNotFoundError:
           msg = "Sorry, the file " + filename + " does not exist!"
           print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file in question has about " + str(num_words) + " words in total!")



filename = "C:/Users/sulem/Desktop/MISC/Python/python_work/text docs/Legend of Mubarak.txt"

count_words(filename)

#To make it fail silently, in the except block simply define a 'pass' statement 
#instead of printing an error message.






