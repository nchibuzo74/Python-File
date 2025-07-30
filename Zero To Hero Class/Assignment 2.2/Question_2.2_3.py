#3. Use a for loop to print all even numbers between 1 and 20 (inclusive).

#Solution:
#Thought Process:
#Create a variable to store the numbers in a list
#Use a for statement to house the range of numbers
#Print all even numbers
#Wrap the logic using error handling mechanism

#Handle Error
try:
    even_numbers = []
    
    for number in range(1,20):
        if number % 2 == 0:
            #Fill the empty variable (even_numbers) with the items in number
            even_numbers.append(number)
            print(even_numbers)

except ValueError:
    print(f'Please enter a number correctly. ')

finally:
    print(f'Thanks for complying. ')