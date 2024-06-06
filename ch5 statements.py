
#5-3 Alien colors



alien_color='blue'
#version that fails
if alien_color == 'green':
    print('Congrats, you earned 5 points!')


#version that passes

'''if alien_color == 'blue':
    print('Congrats, you earned 5 points!')'''

#5-4 Alien Colors #2

if alien_color == 'green':
    print('You earned 5 points')
else:
    print('You earned 0 points')

#5-5 Alien Colors #3

if alien_color == 'green':
    print('You just earned 5 points!')
elif alien_color == 'blue':
    print('You just earned 10 points!')
elif alien_color == 'red':
    print('You earned no points!')

#5-6 Stages of life

age = 17

if age < 2:
    print('baby')
elif (age > 2) and (age < 4):
    print('toddler')
elif (age > 4 ) and (age < 14):
    print('kid')
elif (age > 13) and (age < 20):
    print('teenager')
elif (age > 20) and (age < 65):
    print('adult')
else:
    print('elder')


#5-7 Favorite fruit

favorite_fruits = ['apple', 'orange', 'mango', 'pineapple']

if 'apple' in favorite_fruits:
    print('You really like applies')
if 'grapes' in favorite_fruits:
    print('You really like grapes')
if 'mango' in favorite_fruits:
    print('You really like mangoes')
if 'banana' in favorite_fruits:
    print('You really like bananas')
if 'pineapple' in favorite_fruits:
    print('You really like pineapples')
print('\n')


#tryityourself p89

#5-8 Hello admin

username = ['jsmith', 'admin', 'sjohnson', 'jramirez', 'fthomas']

for x in username:
    if x == 'admin':
        print('You have privileged access.')
    else:
        print('You have normal user rights.')
print('\n')

#5-9 No users

# to test if a list is populated, start the program with 'if list': and then print your statement, your 'else' or 'elif'
# statement will print a statement for your list being empty

#5-10 checking usernames

current_users= ['jsmith', 'agonzalez', 'sjohnson', 'jramirez', 'fthomas']

new_user= ['jramirez', 'ssmith', 'fthomas', 'astevens']

for x in new_user:
    if x in current_users:
        print(f"You have already used the username, {x}.")
    else:
        print("This username is available.")
print("\n")


#5-11 ordinal numbers

#use if elif else chain to cycle through numbers in a list and print out 1st, 2nd, 3rd...

