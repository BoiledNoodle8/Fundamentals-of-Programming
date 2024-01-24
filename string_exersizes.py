# QUESTION 1: Take an input string from the user and create a new string

x = input("Input something: \n" )  # Geting Input where input = x
length = len(x)  # Obtaining the length of the input
mid_pos = int(length /2)  # Need to convert to Int - Finding the Middle position of the input
new_string = x[0] + x[mid_pos] + x[-1]  # adding all that together

print(new_string)  # printing the new string
