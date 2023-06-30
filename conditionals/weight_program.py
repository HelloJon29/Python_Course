# have user enter weight, enter either (k)ilo or (l)bs
# it is not case sensitive
# convert the units and print the result

weight = input('Please enter your weight: ')
unit = input('Enter (K)ilogram or (L)bs: ')
convert_to_kilo = float(weight) * 0.453
convert_to_lbs = float(weight) / 0.453

if unit.upper() == "K":
    print(f'Your weight in Lbs is: {convert_to_lbs}')
elif unit.upper() == "L": # The reason to use elif instead of else here, is because we need the user to only enter either K or L
    print(f'Your weight in Kilos is: {convert_to_kilo}')
else:
    print('You entered invalid info') # Let the user know the info is invalid