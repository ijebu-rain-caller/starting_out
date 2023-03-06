#TRY IT YOURSELF
flag = True

while flag:
    try:
       first_number = input("Input first number(type 'End' to exit prompt): ")
       if first_number == "End":
           break
       second_number = input("Input second number: ")
       if second_number == "End":
           break
       result = int(first_number) + int(second_number)
       print(int(result))
    except ValueError:
        print("Sorry, this prompt only accepts numerical inputs!")

#TRY IT YOURSELF 
filenames = ['cats.txt','dogs.txt']

for files in filenames:
    try:
        with open(files) as pet_file:
          stuff = pet_file.read()
          print(stuff.rstrip())
    except FileNotFoundError:
       pass


#TRY IT YOURSELF
def book_count(filename):
    """Counts the number of times the word 'the' appears"""
    with open(filename) as file_object:
        contents = file_object.read()
        word_count = contents.lower().count('the')
        print(word_count)


filename = ''

book_count(filename)

