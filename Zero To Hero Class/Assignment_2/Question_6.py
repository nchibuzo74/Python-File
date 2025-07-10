"""
Question 6: Write a Python program that computes the greatest common divisor (GCD) of
two positive integers.
"""

#Solution:
"""
Thought Process: 
i. Create a variable to accept users input of two numbers
ii. The first input should be greater than the second input
iii. Create a mechanism to identify the division logic
iv.Create another variable that will store the first number
v. Divide the first number by the second number
vi. Replace the first number with the second number
vii. Replace the second number with the remainder
viii. Repeat until the remainder is 0
"""

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

#Keep looping until second number becomes 0
while second_number != 0:
    #Store the original value of first number
    initial_first_number = first_number
    #Replace first number with second number
    first_number = second_number
    #Replace second number with remainder of initial_first_number divided by second number
    second_number = initial_first_number % second_number
    
    #When second number is 0, first number contain the greater common divisor 
    print(f'The GCD is {first_number}')
