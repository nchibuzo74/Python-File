"""
Write a Python function that accepts two integers as arguments and sums  two integers. 
However, if the sum is between 15 and 20 it will return 20.
"""

#Solution:
#Thought Process:
#Create a variable that accepts the user input of two integers
#Create a mechanism to sum the two integers
#Create a condition to check if the sum is between 15 and 20.
#Wrap the logic using error handling mechanism

#Handle Error
try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    
    #Aggregate the numbers
    total_number = first_number + second_number
    
    #Logic to check if the sum is between 15 and 20
    if total_number >= 15 and total_number <= 20:
        print(20)
    else:
        print(total_number)  # Print the total if the total not in the range 15 - 20
except ValueError:
    print(f'Please enter a number correctly. ')
