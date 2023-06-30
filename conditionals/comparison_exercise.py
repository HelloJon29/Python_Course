# if name is less than 3 characters long print error message
# otherwise if name is more than 50 characters long print error message
# otherwise print acceptence message

first_name = input('Please enter your first name: ')

if len(first_name) < 3:
    print('Name must be at least 3 characters')
elif len(first_name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')

# for the solution, get input from user, use len() function to get the amount of characters and compare <3 and > 50 then print statements