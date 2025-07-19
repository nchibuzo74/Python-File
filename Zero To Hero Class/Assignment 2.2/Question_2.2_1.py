"""
1.Write a Python program to construct the following pattern, using a nested for loop. 
*  
* *  
* * *  
* * * *  
* * * * *  
* * * *  
* * *  
* *  
* 
"""

#Solution:
#Thought Process: 
# Create a varaible to store the list of stars in memory
# Use a for statement to loop the increasing stars within the range of stars
#Print the stars
#Loop again with the for statement to loop the decreasing stars within the range of stars
#Print the stars

# Number of rows in the upper half of the pattern
n = 5

# Upper half (increasing stars)
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line

# Lower half (decreasing stars)
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line


#2. Write a program that uses a for loop to print numbers from 10 down to 1.

#Solution:
#Thought Process:
#Create a variable that stores the number
#Use a for statement to decrease the numbers
#Print the numbers

number = 10

# Lower half (decreasing stars)
for num in range(number, 0, -1):
    print(num)


#3. Use a for loop to print all even numbers between 1 and 20 (inclusive).

#Solution:
#Thought Process:
#Create a variable to store the numbers in a list
#Use a for statement to house the range of numbers
#Print all even numbers

even_numbers = []

for number in range(1,20):
    if number % 2 == 0:
        #Fill the empty variable (even_numbers) with the items in number
        even_numbers.append(number)
        print(even_numbers)


#4. Use a while loop to print all odd numbers between 1 and 15 (inclusive).

#Solution:
#Create a variable to store the numbers in memeory
#Use a while statement to loop the process
#Use an if statement to identify the odd numbers or not
#Print the odd numbers

number = 1  # Start with the first odd number
while number <= 15:  # Continue until we reach 15
    if number % 2 != 0:  # Check if the number is odd
        print(number)
    number = number + 1  # Move to the next number


#5. Write a program that repeatedly asks the user for a number until they enter 0. After they enter 0, 
# print the sum of all the numbers they entered (excluding the 0).

#Solution:
#Thought Process:
#Create a variable to accept users input
#Create a mechanism to identity the number from the user input if it's zero or not
#If enter zero, sum up all the numbers they entered before excluding zero

total = 0

while True:
    user_input = input("Enter a number (0 to stop): ")
    try:
        num = float(user_input)
    except ValueError:
        print("Please enter a valid number")
        continue
    
    if num == 0:
        break
    total += num

print(f"The sum is: {total}")