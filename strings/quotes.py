# Sometimes you have to be selective of the type of quotes used
# course = 'Python's Course for beginners' # this causes errors since the first single quote is closed after Python'
course = "Python's Course for beginners" # using double quotes allows apostrophes
print(course)

# the opposite is also true
# course_2 = "Python for "Beginners""" # the second double quote after for causes errors
course_2 = 'Python for "Beginners"' # Using single quotes allows the use of double quotes within the string
print(course_2)

# This is an example of creating multiple lines of strings using triple quotes

email = '''
Hi Jon,

Quick email to let you know we are testing strings

Thank you,
Support

'''
print(email)