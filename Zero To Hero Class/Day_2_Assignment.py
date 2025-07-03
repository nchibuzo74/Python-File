"""Question 1: Ask the user for their name and favourite colour, then print:
Hello [name], your favourite colour is [colour] ! (Use f-string)
"""

#Solution:
your_name = input("Enter your name: ")
favourite_colour = input("Enter your favourite colour: ")

print(f'Hello {your_name}, your favourite colour is {favourite_colour}!')


"""
Question 2: Prompt for a number. Print whether it's:
- Positive
- Negative
- Zero
"""

#Solution:
number = int(input("Enter any number: "))

if number > 0:
    print(f'The number is postive: {number}')

elif number == 0:
    print(f'The number is Zero: {number}')

else:
    print(f'The number is negative {number}')


"""
Question 3: Write a program to calculate a customer's total bill based on: 
- Quantity
- Price
- Print the result using f-string.
"""
#Solution:
"""
Thought Process: 
i. Create a variable to accept user input:
ii. Create another variable to compute the calculation
"""
Quantity = int(input("Enter the quantity bought: "))
Price = int(input("Enter the sales amount of the product: "))

#Calculate the bill
total_bill = Quantity * Price

print(f'The customer total bill is {total_bill}')


"""
Question 4: Prompt the user to enter their score and:
print grade A (90-100), B (80-89), C (70-79), F (below 70)
"""

#Solution:
"""
Thought Process: 
i. Create a variable to allow users to input
ii. Create a mechanism to identify their grade
"""
Score = int(input("Enter your score: "))

if Score >= 90 and Score <= 100:
    print(f'Grade A')

elif Score >= 80 and Score <= 89:
    print(f'Grade B')

elif Score >= 70 and Score <= 79:
    print(f'Grade C')

else:
    print(f'Grade F')


"""
Question 5: Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

#Solution:
"""
Thought Process: The area of a circle is pi r square (r^2)
- Create a variable to accept the radius inputted by the user
- Let pie be 3.142
"""
pie = 3.142
radius = float(input("Enter the radius: "))
area = ((pie) * (radius * radius))

print(f'The area of a circle is {area}')


"""
Question 6: Write a Python program that computes the greatest common divisor (GCD) of
two positive integers.
"""

#Solution:
"""
Thought Process: 
i. Create a variable to accept users input of two numbers
ii. Divide the numbers
iii. The first input should be greater than the second input
"""

first_number = input(input("Enter the first number: "))
second_number = input(input("Enter the second number: "))vhd

print(first_number)