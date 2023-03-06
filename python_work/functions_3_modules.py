#An import statement tells python to make the code in a module 
#available in the present program.

#You can store functions in a seperate file called a module 
import bombastic

bombastic.build_person('Sule','Mubarak',height='10 inches',school='ABUAD')

print(bombastic.build_person('Sule','Mubarak',height='10 inches',school='ABUAD'))

#To import only specific functions use the syntax provided below
from bombastic import sand_wich

sand_wich('bread','steak','ketchup','mayo')

#Ascribing an alias to a function can be necessary when trying to avoid
#confusion or to shorten the function name
from bombastic import sand_wich as sw

sw('goat meat','ata rodo','bread','ketchup')

#The 'as' alias ascriber can also be used on an entire module instead of 
#just a function 

import bombastic as bum

bum.sand_wich('eja tutu','maggi','salt','sauce')

#To import all the functions stored in a module 
from bombastic import *
#This enables you to use each function without drawing from the entire module
#i.e sandwich() instead of bombastic.sandwich()

#The above should be used carefully or avoided, to avoid mixed up functions from the module 
#and your program.

def function_name(parameter_0, parameter_1='default value')
#The above shows that no spaces should be left between the '=' sign
#on both sides of the sign










