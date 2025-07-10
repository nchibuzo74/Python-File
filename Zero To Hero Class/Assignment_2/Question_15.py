"""
Question 15: Write a program that asks for the user's name and their favorite color. Then, 
use string interpolation to create a personalized greeting,
"""

#Solution:
#Thought Process:
# Create a variable to accept user input for the name and favorite color
# Use f-string to create a personalized greeting
name = input("Enter your name: ")
favourite_color = input("Enter your favourite color: ")
print(f'Hello {name}, your favourite color is {favourite_color}!')
