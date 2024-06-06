#tryityourself p36

'''functiona used in list: .title(), .append(), .extend(), del variable, new_variable= oldvariable.pop(), .remove(), .sort(), (sorted()),
.reverse(), len()'''


#3.1 Names
names=['jonathan', 'thomas', 'ryan', 'steven']
print(names)
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())


#3.2 Greetings
greeting0=f"How are you doing, {names[0].title()}?"
print(greeting0)
greeting1=f"How are you doing, {names[1].title()}?"
print(greeting1)
greeting2=f"How are you doing, {names[2].title()}?"
print(greeting2)
greeting3=f"How are you doing, {names[3].title()}?"
print(greeting3)

#3.3 Your Own List
vehicle=['car', 'truck', 'van', 'motorcycle']
print(vehicle)
message=f"I need to own a {vehicle[0]} to get back and forth to work."
print(message)

#.append

names.append('nathan')
print(names)

#insert element to any position of list with .insert and position
names.insert(1, 'timothy')
print(names)

#removing item from list with del
del names[0]
print(names)

# pop()  "popping an item off the top of the stack" removes an item off the end of a list
popped_name=names.pop()
print(popped_name.title())

print(names)

#can use pop() to remove item from anywhere on list by including index in paranthesis

popped_name2=names.pop(0)
print(names)
print(popped_name2)

#remove an item by value with remove()...has to match name in list ('')
names.remove('ryan')
print(names)


extra_names=('ryan', 'thomas')
names.extend(extra_names)
print(names)

#we can also remove a value from a list by an assigned variable
dont_like='thomas'
names.remove(dont_like)
#this can help provide a reason for its removal
print(names)
print(f"I no longer speak with {dont_like.title()} because I don't like him anymore")

#the remove() function only works to remove an item the first time its seen in a list. will need to use a loop to get everything

#Organizing lists

# sort() changes a list to alphabetical order permanently
#can never revert back to the original order after sort()

letters=['a', 'f', 'c', 'k', 'b']
print(letters)
letters.sort()
print(letters)
#reverse=True sorts in reverse alphabetical order
letters.sort(reverse=True)
print(letters)

#(sorted()) will temporarily sort the list

print(sorted(letters))
print(letters)
#sorted() function can also accept (reverse=True)

# print(letters.sort()) does not work for some reason
print(letters.sort())

letters.sort()
print(letters)
print(sorted(letters, reverse=True))

#reverse order
print(letters)
letters.reverse()
print(letters)

#reverse() permanently reverses the order of a list, but you can change it back by using reverse() again

#find how many items are in a list with len()
print(len(letters))






