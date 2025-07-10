#Question 9: Write a Python program to parse a string to float or integer.

#Solution:
#Thought Process: 
# Create a variable to accept user input
# Create a mechanism to check if the input is an integer or float

enter_value = float(input("Enter a number: "))

print(enter_value) #This will automatically convert the input to float if it contains a decimal point.
print(type(enter_value)) #This will show the datatype of the variable.