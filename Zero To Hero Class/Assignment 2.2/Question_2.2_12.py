"""
Write a Python program to count the number of even and odd numbers in a series of 
numbers 
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
"""

#Solution:
#Thought Process:
# Create a tuple of numbers
# Initialize counters for even and odd numbers
# Use a for loop to iterate through the numbers
# Check if each number is even or odd and update the counters accordingly

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
       # print(f'The even numbers are: {numb}')
       
    else:
        odd_count += 1
       # print(f'The odd numbers are: {even_count}')

print(f'Total even numbers: {even_count}')
print(f'Total odd numbers: {odd_count}')