import json

filename = 'fave_no.json'

with open(filename) as file_o:
    message = json.load(file_o)
    print("I know your favorite number! It is ....." + message)


#TRY IT YOURSELF
filename = 'fave_no.json'

fave_number = input("What's your favorite number? ")

with open(filename,'w') as file_object:
    json.dump(fave_number,file_object)
    print("Your favorite number has been stored!")

filename = 'fave_no.json'

try:
    with open(filename) as file_o:
        message = json.load(file_o)
        print("I know your favorite number! It is ....." + message)
except FileNotFoundError:
    f_n = input("What is your favorite number? ")
    with open(filename,'w') as f_o:
        json.dump(f_n,f_o)


    
    


