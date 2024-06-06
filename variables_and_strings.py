first_name="raymond"
last_name="jaure"

#this is called an f-string, the f will format the variable in the braces
full_name=f"{first_name} {last_name}"
print(full_name)

print(f"Hello, my name is {full_name.title()}")

message=f"Hello, my name is {full_name.title()}"
print(message)

full_name=f"{last_name}, {first_name}"
print(full_name)

full_name=first_name + last_name
print(full_name)

#f-strings were introduced in Python 3.6, anything earlier and you nee to use format()
# full_name = "{} {}".format(first_name, last_name}

full_name = "{} {}".format(first_name, last_name)
print(full_name)
print(full_name.title())

