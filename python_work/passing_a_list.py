def greet_users(names):
    """Sending a greeting to all the provided names in a list"""
    for name in names:
        print("Hello!, " + name.title())

users = ['barakah','islamiyah','quadri']
greet_users(names = users)


#Modifying a list in a function 
#Example without a function 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
printed_designs = []

while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print("Printing designs....")
    print("Printing model: " + current_designs)
    printed_designs.append(current_designs)

print("\nThe following models have been printed: ")
for printed in printed_designs:
    print(printed)


#Example with a function call 
def print_models(unprinted_designs,printed_designs):
    """Simulates the printing of each design until none are left"""
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print("Printing model: " + current_designs)
        printed_designs.append(current_designs)

def show_completed_design(printed_designs):
    """This functions objective is to show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for printed in printed_designs:
        print(printed)
    
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
printed_designs = []

print_models(unprinted_designs,printed_designs)
show_completed_design(printed_designs)

#To only use a copy of the list without modifying, use the python
#slice [:] feature on the list in the function call.

#TRY IT YOURSELF 
magician_names = ['houdini','babs cardini','chris angel','dynamo']

def show_magicians(magician_names):
    """Prints the name of each magician in the list provided"""
    print("The list of magicians are: ")
    for magician in magician_names:
        print(magician.title())

show_magicians(magician_names)


magician_names = ['houdini','babs cardini','chris angel','dynamo']

def show_magicians(magician_names):
    """Prints the name of each magician in the list provided"""
    print("The list of magicians are: ")
    for magician in magician_names:
        print(magician.title())

def make_great(magician_names):
    """Are you really great if you have to be called great?"""
    print("\nThe list of 'great' magicians are: ")
    for magician in magician_names:
        print("The Great " + magician.title())


make_great(magician_names[:])

new_list = magician_names[:]
show_magicians(magician_names)
show_magicians(new_list)









    

