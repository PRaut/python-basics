#!/bin/python3

import sys # system functions and params
#from datetime import datetime #imports datetime from datetime module
from datetime import datetime as dt # import as alias

print(sys.version)
#print(datetime.now())
print(dt.now())

myname = "John"
print(myname[0]) # prints 1st letter
print(myname[-1]) # prints last letter

fullName = "My name is John"
splitted_fullname = fullName.split()
print(splitted_fullname) # splits on "" and return a list

myFullName = ' '.join(splitted_fullname) 
print(myFullName)

quote = "He said, \" Give me all your money\""
print(quote)

too_much_space = "                hello"
print(too_much_space.strip()) # strip() removes extra spaces

print("A" in "Apple")  # return True 

# Formatting the  string
movie = "The Hangover"
print("My favorite movie {}.".format(movie))

#Dictionary - key/value pairs  {}

drinks = { "white russian": 7 , "Old fashion": 10, "Lemon drop": 8}
print(drinks)

print(drinks['Lemon drop']) # Get Value using key

drinks['Kokam'] = ['5'] # Add Key/Value in Dictionary
print(drinks)

drinks['white russian'] = 8 # update value
print(drinks)	