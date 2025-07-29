"""Question 1: Ask the user for their name and favourite colour, then print:
Hello [name], your favourite colour is [colour] ! (Use f-string)
"""

#Solution:
#Thought Process:
#Create a variable accepting user input
#Create a mechanism to identify the user input must be only letters and not number
#Wrap the logic using error handling mechanism

#Handle Error  
try:
    your_name = input("Enter your name: ")
    favourite_colour = input("Enter your favourite colour: ")
    
    #Check if the input for your_name is a letter and not number. If it's number it's invalid
    float(your_name)
    print(f'Invalid! This is a number. ')

#ValueError is used to identify number    
except ValueError:
    #Check if the input for your_name is a letter and not number
    if your_name.isalpha():
        print(f'Hello {your_name}, your favourite colour is {favourite_colour}!')

    else:
        print(f'Invalid! Please enter only letters and state your name and favourite colour correctly. ')

#Greetings
finally:
    print(f'Thank you for complying. ')