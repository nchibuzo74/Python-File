#Write a Python function to sum all the numbers in a list. Sample List : (8, 2, 3, 0, 7)

#Solution:
# Thought Process:
# Create a list of numbers
# Sum the total of the numbers in the list
#Wrap the logic using error handling mechanism

#Handle Error
try:
    list_numbers = (8, 2, 3, 0, 7)
    total_sum = sum(list_numbers)
    print(f"The sum of the numbers in the list is: {total_sum}")
except TypeError:
    print(f'Please enter a number correctly. ')