
months = open('writing_files.txt')

print(months)
"""print(months.mode)
print(months.readable())"""

print(months.read())

#print("\n")
months.seek(0)



#print(months.readline()) #doesn't seem to work


for month in months:
    print(month.strip()) #takes new line out of previous printout, which was double spaced

months.close() #best practice is to close out this process after open on line 2

days = open("days.txt", "a") #"w" puts this in write mode
#to append to a file, the "w" needs to be changed to an "a"

print(days.mode)

#days.write("Monday") #nothing will be output with this script, but it will write this string to days.txt
#days.write will write to the file, not append


days.write("\nWednesday")

#to append, we stick with days.write(), but in our open statement days=open("days.txt", we need to be in append mode or "a")


days.close()

# in open function, we have our text file and then our mode...(.txt file, "w" for write, "r" for read, "a" for append)



