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
