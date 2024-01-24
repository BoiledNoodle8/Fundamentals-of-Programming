## Adding a comment in remote Repo 
'''
# Do not use reserved keywords for variable name
print('Hello World')
print(help('keywords'))


# try to avoid multiple variable declaration simultaneously
a = b = c = 10 # shortcut for below

a = 10
b = 10
c = 10

print(a,b,c)


#Statement vs expression
x = 47  # statement
y = x + 10  #expression 


# Type Conversion --> changing data type of a variable
#Convert floats and numeric strings to int
print(int('20'))
print(int(30))
print(type(int('20')))

print(int(14.21))

# Errors out cause int expects only whole numbers in quotes
# print(int('20.24'))
print(int(float('20.24')))


## STRINGS ##
# 3 ways to create a string - using either single, double, or triple quotes
first_name = 'Jane'
last_name = 'Doe'
address = "10 Main St."
job = "physician's Assistant" # Reccomended to use double quotes for strings

## STRING FUNCTIONS##
# len() --> Returns number of characters in a string
print(len("Hello"))

# Upper and Lower --> convert string to appropriate case
print("Hello" .upper())

# String Concatenation - adding up stings
first_name = "Jane"
last_name = "Doe"

print(first_name + ' ' + last_name)

age = 24

print(first_name + ' ' + last_name + ":" + ' ' + str(age))

# String Multiplication --> Multiply a string with an int
print("Hello"*3)
'''
# Accessing string characters - a sting is just a sequence of characters

name = "Jane Doe"
print(name[2])
# print(name[8]) # Throws index out of bounds error


# Retrieving a character at a given index
print(name.index('o')) # Returns 6
print(name.index('e')) # returns index of first occurance
