course = 'Python for Beginners'
# index:  012345

# we can use brackets to return the designated indicies, in this case the char P in the string at index 0
print(course[0])

# we can also use negative index numbers as well, -1 will return the last char in the string
print(course[-1]) #negative numbers will go backwards from the end of the array starting at -1

# Can also extract a range of numbers using :
print(course[0:3]) # this is exlusionary, meaning it won't return the value at index 3
print(course[0:]) # without the 2nd parameter, this will run to the end of the string
print(course[1:]) # this will start at the 1 index and run to the end, excludes 0 index
print(course[:5]) # without a start index, python assumes 0 is the parameter
print(course[:]) # this will assume 0 is the start and then run through the whole string, this is a way to copy a string or array
