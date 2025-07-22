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