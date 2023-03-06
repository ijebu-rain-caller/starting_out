with open('text docs\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#The above describes a method when trying to access an alternative file path
#to the one where python files are stored.

#The above style uses a relative path (relative to the default python work folder)

#Using an absolute file path, you can read files from any location
#on your system/pc.
file_path = 'C:/Users/sulem/Desktop/MISC/Python/python_work/text docs/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print('\n' + contents)

#NB: The with syntax tells python to open and close the file properly.
filename = 'C:/Users/sulem/Desktop/MISC/Python/python_work/text docs/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

