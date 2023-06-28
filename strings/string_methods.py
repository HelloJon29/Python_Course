course = 'Python for Beginners'
print(len(course)) #this len() finds the number of characters in the String, general purpose function for many things
print(course.upper()) #this is an example of a Method in Python, a function that belonds to something, in this case Strings
print(course.lower())

print(course.find('P')) #find method returns the index of the first matching character given, if no match returns -1
print(course.find('Beginners')) # Can also pass a sequence of characters, returns the first index where the matching word begins 
print(course.replace('Beginners', 'Absolute Beginners')) # Replaces the passed in string with a new one

print('python' in course) #this is a boolean expression returns True or False, case sensitive