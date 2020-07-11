#!/bin/python3

#Variables and Methods
quote = "All is fair in love and war"
print(quote)
print(quote.upper()) # upper case
print(quote.lower()) # lower case
print(quote.title()) # title case
print(len(quote))    # length of the string

name = "John" # string
age = 30 # int
gpa = 3.7 # float float(3.7)

print(age)
print(gpa)

print(int(30.9)) # prints only 30 and doesn't round
# convert int to string using str() like we do for int(val) and float(val)
# otherwise it gives error
print("My name is "+ name + " and I am "+ str(age) + " years old")

print('\n')
print("Functions Examples")

# This is a function
def who_am_i():
	name = "Adam"
	age = 30
	print("My name is "+ name + " and I am "+ str(age) + " years old")		

who_am_i()

# Single Param
def add_100(num):
	print(num + 100);

add_100(100)

# Multiple Param
def add(x,y):
	print(x+y)
	
add(10,20)

def multiply(x,y):
	return (x*y)

mul = multiply(10,5)
print(mul)

def square_root(x):
	print(x** .5)

square_root(64)

print('\n')
#Boolean Expression

bool1 = True
# type(val) returns type of value < class 'bool'>
print(type(bool1), bool1)
bool2 = 3*3 ==9
bool3 = False
bool4 = 3*3 != 9

print('\n')
#Relational and Boolean operator >, <, <=, >=, and , or, not
greater_than = 7 > 5
print(greater_than)

test = not True #False
print(test)

print('\n')
#Conditional Statements if else, if elseif
def drink(money):
	if money >= 2:
		return "You've got yourself a drink"
	else:
		return "No drink for you"

print(drink(2))

def alcohol(age, money):
	if (age >= 21) and (money >= 5):
		return "we're getting alcohol for you"
	elif (age >= 21) and (money < 5):
		return "Come back with more money"
	elif (age < 21) and (money >=5):
		return "nice try kid"
	else:
		return "You're too poor and too young"

print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 5))
print(alcohol(20, 4))

