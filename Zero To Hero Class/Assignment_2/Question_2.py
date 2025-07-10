"""
Question 2: Prompt for a number. Print whether it's:
- Positive
- Negative
- Zero
"""

#Solution:
number = int(input("Enter any number: "))

if number > 0:
    print(f'The number is postive: {number}')

elif number == 0:
    print(f'The number is Zero: {number}')

else:
    print(f'The number is negative {number}')