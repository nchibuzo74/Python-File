"""
Question 13: Write a Python program to check if a triangle is equilateral, isosceles or scalene.  
Note : 
An equilateral triangle is a triangle in which all three sides are equal. 
A scalene triangle is a triangle that has three unequal sides. 
An isosceles triangle is a triangle with (at least) two equal sides.
"""

#Solution:
#Thought Process: Create a variable to accept user input for the three sides of the triangle
# Create a mechanism to check the type of triangle based on the sides
# Wrap the logic using error handling mechanism

def triangle_type(a, b, c):
    # Check if it's a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle!"
    
    # Check the type
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Handle Error
try:    
    # Input sides
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))
    
    # Get and print the result
    result = triangle_type(a, b, c)
    print(f"The triangle is: {result}")

except ValueError:
    print('Please enter a number correctly.')
