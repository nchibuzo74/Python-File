"""
Question 7: Write a Python program to find the least common multiple (LCM) of two positive 
integers. enter by the user from the terminal.
"""

#Solution:
"""
Thought Process:
- Create a variable taking user input
- Create a variable to find the greater number between two numbers
- Check multiples if greater number is divisible by both numbers.
- Wrap the logic using error handling mechanism
"""

#Handle Error
# Handle Error
try:
    # Take input from the user
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    
    # Find the greater number
    greater_number = max(number1, number2)
    
    # Keep checking multiples of the greater number until divisible by both
    while True:
        if greater_number % number1 == 0 and greater_number % number2 == 0:
            lcm = greater_number
            break
        greater_number += 1
    
    # Print the result after finding LCM
    print(f'The LCM of {number1} and {number2} is {lcm}')

except ValueError:
    print('Please enter a correct number.')

# Greetings
finally:
    print('Thank you for complying.')
