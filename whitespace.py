#\t is a new tab, \n is a new line
# .strip() removes whitespace, .rstrip() and .lstrip() remove whitespace to left and right of string

my_children="Chase Jaure\nLayla Jaure\nNoelle Jaure"
print(my_children)

my_family="Raymond Jaure\nKari Jaure\n\tChase Jaure\n\tLayla Jaure\n\tNoelle Jaure"
print(my_family)

space_before=" there is a space before"
print(space_before)
print(space_before.lstrip())

space_after="there is a space after "
print(space_after)
print(space_after.rstrip())

space_before_and_after=" there is a space before and after "
print(space_before_and_after)
print(space_before_and_after.strip())