is_hot = False
is_cold = True

if is_hot: # to begin a condional, use a : after the boolean statement
    print("it's a hot day") # this indent is the code block for the if statement
    print("Please drink plenty of water")
elif is_cold: # elif is an else if statement
    print("it's a cold day")
    print("wear warm clothes")
else: # elses will run parallel to the if statement as shown here
    print("it's a lovely day")
print("it's Enjoy your day") # without the indent we are now out of the block