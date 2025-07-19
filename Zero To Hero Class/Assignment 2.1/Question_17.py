#Question 17:  Write a program that takes three numbers as input and prints the largest one using if-elif-else. 

#Solution:
#Thought Process: 
# Create a variable to accept user input for the three numbers
# Create a mechanism to check the largest number

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

maximum_number = max(number_1,number_2,number_3)

if maximum_number > 0:
    print(f'The largest number is {maximum_number}')

else:
    print(f'There is no largest number')
