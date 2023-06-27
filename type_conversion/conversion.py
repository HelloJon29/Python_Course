birth_year = input('Birth year: ') # Typing into terminal is always treated as a String with input()
print(type(birth_year))
#age = 2023 - birth_year # as is this causes an error because of type mismatch, int and string
age = 2023 - int(birth_year)
print(type(age))
print(age)

# some functions for conversion: int(), float(), bool()