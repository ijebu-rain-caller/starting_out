strains = ['Sativa', 'Indica', 'Hybrid']
print(strains)

#The -1 represents the last element in the list, helpful lists with a lot of elements 
# -2 = second to the last, and so on and so forth
print(strains[-1])

print("These types of cannabis are available:" + "\n\t1." + strains[0] )

names = ['Benjy', 'Kaka', 'Stelmaria', 'Bonaventure']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
 
message = "Hope you're having a lovely day " + names[0]
print(message)

names.append('asriel')
print(names)

cookies = []
cookies.append('chocolate chip')
cookies.append('Hazel Nut')
cookies.append('Coconut Chip')
cookies.insert(2,'Strawberry')
print(cookies)

del cookies[1]
print(cookies)

popped_cookie = cookies.pop()
print(popped_cookie)

print("The last cookie I ate was a " + popped_cookie + " cookie!")


