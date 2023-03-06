myfile = 'C:/Users/sulem/Desktop/MISC/Python/python_work/text docs/pi_digits.txt'

with open(myfile) as my_file:
    lines_from_file = my_file.readlines()

for lines in lines_from_file:
    print(lines.rstrip())


#The readlines() method stores the information contained in the file line by line in a list

pi_string = ''
for line in lines_from_file:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#The above allows you to print all the contents of the list as a single 
#string. 
#The len fxn tells us the length of all characters in the particular
#string. 

file_path = 'C:/Users/sulem/Desktop/MISC/Python/python_work/text docs/infoaboutpy.txt'

with open(file_path) as try_text:
    new_try_text = try_text.read()
    print(new_try_text.rstrip() + '\n')
    
with open(file_path) as try_text:
    new_try_text = try_text.readlines()

for lines in new_try_text:
    print(lines.rstrip())


#Using the replace command with strings
message = 'I did not vote for Tinubu'
message.replace('Tinubu','Atiku')
message = message.replace('Tinubu','Atiku')
print(message)


with open(file_path) as try_text:
    new_try_text = try_text.read()
    newer_try_text = new_try_text.replace('python','C')
    print(newer_try_text.rstrip() + '\n')

    




    









