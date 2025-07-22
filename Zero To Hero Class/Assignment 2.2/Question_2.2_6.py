"""
6. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 
Note : Use 'continue' statement.
"""

#Solution:
#Thought Process:
#Create a loop to iterate through the numbers from 0 to 6

for number in range(7):
    if number == 3 or number == 6:
        continue #Skip the 3 and 6
    print(f'The numbers are: {number}')