"""
Question 2: Prompt for a number. Print whether it's:
- Positive
- Negative
- Zero
"""

#Solution:
#Thought Process:
#Create a variable to accept user input.
#Create a condition to check if the number is positive, negative, or zero.
#Print the result based on the condition.
#Wrap the logic using error handling mechanism

#Handles errors
try:
    number = int(input("Enter any number: "))
    
    if number > 0:
        print(f'The number is postive: {number}')
        
        if number == 0:
            print(f'The number is Zero: {number}')
            
            if number < 0:
                print(f'The number is negative {number}')

except ValueError:
    print(f'Please enter the number correctly.')