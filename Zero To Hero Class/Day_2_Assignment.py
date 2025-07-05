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
ii. The first input should be greater than the second input
iii. Create a mechanism to identify the division logic
iv.Create another variable that will store the first number
v. Divide the first number by the second number
vi. Replace the first number with the second number
vii. Replace the second number with the remainder
viii. Repeat until the remainder is 0
"""

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

#Keep looping until second number becomes 0
while second_number != 0:
    #Store the original value of first number
    initial_first_number = first_number
    #Replace first number with second number
    first_number = second_number
    #Replace second number with remainder of initial_first_number divided by second number
    second_number = initial_first_number % second_number
    
    #When second number is 0, first number contain the greater common divisor 
    print(f'The GCD is {first_number}')


"""
Question 7: Write a Python program to find the least common multiple (LCM) of two positive 
integers. enter by the user from the terminal.
"""

#Solution:
"""
Thought Process:
- Create a variable taking user input
- Create a variable to find the greater number between two numbers
- Check multiples if greater number is divisible by both numbers.
"""
# Take input from the user
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Find the greater number
greater_number = max(number1, number2)

# Keep checking multiples of the greater number until divisible by both
while True:
    if greater_number % number1 == 0 and greater_number % number2 == 0:
        lcm = greater_number
        break
    greater_number += 1

print(f"The LCM of {number1} and {number2} is {lcm}")


"""
Question 8: Write a Python program to compute the future value of a specified principal 
amount, rate of interest, and number of years. (calculate simple interest based on 
user input)
"""

#Solution:
"""
Thought Process: 
- The formula for simple interest is (P * R * T) / 100
- Create a variable accepting user input - principal, rate and time
- Create a varaible to compute the calculation
"""
Principal = int(input("Enter the Principal amount: "))
Rate = int(input("Enter the Rate (%): "))
Time = int(input("Enter the Time (in years): "))

SI = (Principal * Rate * Time) / 100

print(f'The Simple Interest is {SI}')


#Question 9: Write a Python program to parse a string to float or integer.

#Solution:
#Thought Process: 
# Create a variable to accept user input
# Create a mechanism to check if the input is an integer or float

enter_value = float(input("Enter a number: "))

print(enter_value) #This will automatically convert the input to float if it contains a decimal point.
print(type(enter_value)) #This will show the datatype of the variable.


#Question 10: Write a Python program to convert height (in feet and inches) to centimeters.

#Solution:
"""
Thought Process:
- Create a variable to accept user input for feet and inches
- Convert feet to centimeters (1 foot = 30.48 cm)
- Convert inches to centimeters (1 inch = 2.54 cm)
- Create a mechanism to compute the total height in centimeters
"""

feet_value = float(input("Enter your height in feet: "))
inches_value = float(input("Enter your height in inches: "))

# Conversion factors
one_foot_to_cm = 30.48
one_inch_to_cm = 2.54

#Mechanism to compute the total height in centimeters
height = ((feet_value * one_foot_to_cm) + (inches_value * one_inch_to_cm))

print(f'The convertion of height (in feet and inches) to centimeters is {height}')
