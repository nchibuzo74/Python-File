#Question 11:  Write a Python program to calculate the hypotenuse of a right angled triangle.

#Solution:
#Thought Process: The formula for calculating the hypotenuse is: c = sqrt(a^2 + b^2)
# - Create a variable to accept user input for the two sides of the triangle
# Wrap the logic using error handling mechanism

#Handle Error
try:
    first_number = int(input("Enter the first side of the triangle: "))
    second_number = int(input("Enter the second side of the triangle: "))
    
    hypotenuse = (((first_number ** 2) + (second_number ** 2)) ** 0.5)
    
    print(f'The hypotenuse of the right angled triangle is {hypotenuse}')

except ValueError:
    print(f'Please enter a number correctly. ')
