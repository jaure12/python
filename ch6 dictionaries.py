#dictionaries are basically lists but with key:value pairs inside

alien_0 = {'color': 'green', 'points': 5}

#tuples use parentheses, dictionaries use curly braces, lists use square brackets

#refer to the item in the dictionary with square brackets: print(alien_0['color']

#adding new values

#you can also start with an empty dictionary alien_0={}
print(alien_0)
print('\n')


alien_0['x_position'] = 0
alien_0['y_position'] = 24
print(alien_0)

#change the color of the dictionary value

print(alien_0['color'])

alien_0['color'] = 'blue'

print(alien_0['color'])

alien_0['speed']= 'low'
print(alien_0)

if alien_0['speed'] == 'low':
    x_increment = 5
else:
    x_increment = 1
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(alien_0)

del alien_0['points'] #delete key value from data dictionary
print(alien_0)

#using get(), will create a default value if value does not exist

point_value = alien_0.get('points', 'No points exist, sorry')
print(point_value)

point_value = alien_0.get('points') #will return 'None' if no default value is listed
print(point_value)

#try it yourself p 99

#6-1 person

steven_olsen = {'first_name': 'Steven', 'last_name': 'Olsen', 'Age': 32, 'City': 'San Antonio'}
print(steven_olsen['first_name'])
print(steven_olsen['last_name'])
print(steven_olsen['Age'])
print(steven_olsen['City'])
print(steven_olsen)

#6-2 Favorite Numbers

favorite_number = {
    'Steven': 2,
    'Tom': 8,
    'John': 9,
    'Anthony': 6,
    'Kevin': 1,
}

print(favorite_number['Steven'])
print(favorite_number['Tom'])
print(favorite_number['John'])
print(favorite_number['Anthony'])
print(favorite_number['Kevin'])

#6-3 Glossary

user0={
    'first_name': 'John',
    'last_name': 'Smith',
    'age': 21,
}

for k, v in user0.items(): #key and value were replaced with k and v....have to declare .items() for the items in the
    #dictionary
    print(f"\nKey: {k.title()}") #key variable has to be replaced with k
    print(f"Value: {v}") #value variable has to be replace with v

#can replace key, value with any other variable, just stay constant in the loop

for beginning, end in user0.items(): #key and value were replaced with beginning and end....have to declare .items() for the items
    # in the dictionary
    print(f"\nKey: {beginning.title()}") #key variable was replaced with beginning
    print(f"Value: {end}") #value variable was replaced with end

#looping through all keys in a dictionary with .keys() method

for x in user0.keys():
    print(f"The key value in this dictionary is {x.title()}\n")

#looping through the keys in a dictionary is default behavior...is .keys() needed?

for x in user0:
    print(f"The key in this dictionary is {x.title()}\n") #.keys() is not needed but probably helps understand
    #what is being done

for x in user0.values():
    print(f"the value in this dictionary is {x}")

for x in sorted(user0.keys()): #use the sorted() method to temporarily put the keys/values in alphabetical order
    print(f"These keys are now in alphabetical order: {x}")

# we can loop through a list in a dictionary, but to only show unique items, not repetitive, we will use set()
# set(user0.values()) or set(user0.keys())

#can build a set with curly braces and commas instead of key value pairs....is it still a dictionary?

languages={'python', 'C', 'Java'}
print(languages)

#try it yourself p 105

#6-5 Rivers

rivers = {'nile': 'egypt', 'mississippi': 'united states', 'amazon': 'brazil'}

for river, country in rivers.items():
    print(f"\nThe {river.title()} river runs through {country.title()}.")

for river in rivers.keys():
    print(f"\n{river.title()}")

for country in rivers.values():
    print(f"\n{country.title()}")

#6-6 Polling


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'thomas', 'phil']


for name in people:
    if name in favorite_languages.keys():
        print(f"Thank you, {name.title()}, for answering our poll!")
    else:
        print(f"{name.title()}, can you please take our poll?")

#Nesting

#try it yourself p 112

#6-7 People

'''
steven_olsen = {'first_name': 'Steven', 'last_name': 'Olsen', 'Age': 32, 'City': 'San Antonio'}
print(steven_olsen['first_name'])
print(steven_olsen['last_name'])
print(steven_olsen['Age'])
print(steven_olsen['City'])
print(steven_olsen)'''

john_thomas = {'first_name': 'John', 'last_name': 'Thomat', 'Age': 43, 'City': 'Denver'}
jennifer_smith = {'first_name': 'Jennifer', 'last_name': 'Smith', 'Age': 31, 'City': 'Tampa'}

people = ['steven_olsen', 'john_thomas', 'jennifer_smith']
print(people)
for first_name in people.items():
    print(first_name)

#6-8 Pets


#6-9 Favorite Places


#6-10 Favorite Numbers


#6-11 Cities


#6-12 Extensions





