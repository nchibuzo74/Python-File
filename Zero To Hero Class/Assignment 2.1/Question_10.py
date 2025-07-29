#Question 10: Write a Python program to convert height (in feet and inches) to centimeters.

#Solution:
"""
Thought Process: The formula for converting feet and inches to centimeters is: (feet * 30.48) + (inches * 2.54)
- Create a variable to accept user input for feet and inches
- Convert feet to centimeters (1 foot = 30.48 cm)
- Convert inches to centimeters (1 inch = 2.54 cm)
- Create a mechanism to compute the total height in centimeters
- Wrap the logic using error handling mechanism
"""

#Handle Error
try:
    feet_value = float(input("Enter your height in feet: "))
    inches_value = float(input("Enter your height in inches: "))
    
    # Conversion factors
    one_foot_to_cm = 30.48
    one_inch_to_cm = 2.54
    
    #Mechanism to compute the total height in centimeters
    height = ((feet_value * one_foot_to_cm) + (inches_value * one_inch_to_cm))
    
    print(f'The convertion of height (in feet and inches) to centimeters is {height} cm')

except ValueError:
    print(f'Please enter a number correctly. ')

#Greetings
finally:
    print(f'Thank you for complying. ')
