"""
10. Write a Python program to print the alphabet pattern 'E'. 
Expected Output: 
*****                                                                   
*                                                                       
*                                                                       
****                                                                    
*                                                                       
*                                                                       
*****
"""

#Solution:
#Thought Process:
#Create a loop to iterate through the number of rows
#Cres=ate a mechanism to print '*' for the first, fourth, and last rows
# Define the pattern for 'E' as a list of strings

numbers = 7
for number in range(numbers):
    # Create a mechanism to print '*' for the first, fourth, and last rows
    if number == 0 or number == 3 or number == 6:
        print("*" * 5)  # Print five stars for the top, middle, and bottom rows
    else:
        print("*")  # Print a single star for the vertical lines