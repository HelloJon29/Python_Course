#
first_name = 'John'
last_name = 'Johnson'
message = first_name + ' [' + last_name + '] is a coder' # this is unformatted, have to concatinate each part
msg = f'{first_name} [{last_name}] is a coder' #this is a formatted string where you can use curly braces to append variables into it
print(msg)