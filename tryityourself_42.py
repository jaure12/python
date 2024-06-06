#3-4 Guest List

guest_list=['Tom Sawyer', 'Stephen Hawking', 'Jesus Christ']
message=f"This invitation kindly invites {guest_list[0]} to dinner tonight."
print(message)

message=f"This invitation kindly invites {guest_list[1]} to dinner tonight."
print(message)

message=f"This invitation kindly invites {guest_list[2]} to dinner tonight."
print(message)

#message=f"This invitation kindly invites {guest_list[0], guest_list[1], guest_list[2]} to dinner tonight."
#print(message)

#3-5 Changing Guest list

print(f"I am sorry to announce that {guest_list.pop(1)} will not be able to attend dinner tonight.")

print(guest_list)
guest_list.insert(1, 'John Kennedy')
print(guest_list)

message=f"This invitation kindly invites {guest_list[0]} to dinner tonight."
print(message)

message=f"This invitation kindly invites {guest_list[1]} to dinner tonight."
print(message)

message=f"This invitation kindly invites {guest_list[2]} to dinner tonight."
print(message)

#3.6 More Guests

#additional_guests={'John', 'Bueller', 'Jenkins'}
#.append adds the new names as a bracketted list, so we have to use .extend to have the new guests displayed as individuals
#guest_list.extend(additional_guests)

guest_list.insert(0, 'John')
guest_list.insert(2, 'Bueller')
guest_list.insert(-1, 'Jenkins')

print(guest_list)

#exercise required me to print a new statement for each guest, I decided to use a for loop
for x in guest_list:
    print(f"This invitation kindly invites {x} to dinner tonight.")

#3.7 shrinking guest list

remove_guest1=guest_list.pop()
print(guest_list)
print(f"{remove_guest1}, I am sorry to inform you that you are no longer invited to dinner.")

remove_guest2=guest_list.pop()
print(guest_list)
print(f"{remove_guest2}, I am sorry to inform you that you are no longer invited to dinner.")

remove_guest3=guest_list.pop()
print(guest_list)
print(f"{remove_guest3}, I am sorry to inform you that you are no longer invited to dinner.")

remove_guest4=guest_list.pop()
print(guest_list)
print(f"{remove_guest4}, I am sorry to inform you that you are no longer invited to dinner.")

for x in guest_list:
    print(f"This invitation kindly invites {x} to dinner tonight.")

del guest_list[0]
print(guest_list)

del guest_list[0]
print(guest_list)