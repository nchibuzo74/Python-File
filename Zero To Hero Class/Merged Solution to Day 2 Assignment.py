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
Thought Process: The formula for converting feet and inches to centimeters is: (feet * 30.48) + (inches * 2.54)
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

print(f'The convertion of height (in feet and inches) to centimeters is {height} cm')


#Question 11:  Write a Python program to calculate the hypotenuse of a right angled triangle.

#Solution:
#Thought Process: The formula for calculating the hypotenuse is: c = sqrt(a^2 + b^2)
# - Create a variable to accept user input for the two sides of the triangle

first_number = int(input("Enter the first side of the triangle: "))
second_number = int(input("Enter the second side of the triangle: "))

hypotenuse = (((first_number ** 2) + (second_number ** 2)) ** 0.5)

print(f'The hypotenuse of the right angled triangle is {hypotenuse}')


"""
Question 12: Write a Python program to check the validity of passwords input by users.
Validation:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.

Solution:
Thought Process: 
- Create a function to validate the password
- Use string methods to check for the presence of lowercase, uppercase, digits, and special characters
- Create a variable to accept user input for the password
- Create a mechanism to check the validity of the password based on the given conditions
"""

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in {'$', '#', '@'} for char in password)
    
    return {has_lower} and {has_upper} and {has_digit} and {has_special}

# Test the function
password = input("Enter password: ")
if validate_password(password):
    print("Password is valid!")
else:
    print("Password is invalid!")


"""
Question 13: Write a Python program to check if a triangle is equilateral, isosceles or scalene.  
Note : 
An equilateral triangle is a triangle in which all three sides are equal. 
A scalene triangle is a triangle that has three unequal sides. 
An isosceles triangle is a triangle with (at least) two equal sides.
"""

#Solution:
#Thought Process: Create a variable to accept user input for the three sides of the triangle
# Create a mechanism to check the type of triangle based on the sides

def triangle_type(a, b, c):
    # Check if it's a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle!"
    
    # Check the type
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Input sides
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Get and print the result
result = triangle_type(a, b, c)
print(f"The triangle is: {result}")


"""
Question 14: Write a Python program that reads two integers representing a month and 
day and prints the season for that month and day. 
Expected Output: 
Input the month (e.g. January, February etc.): july                      
Input the day: 31                                                        
Season is harmattan
"""

#Solution:
#Thought Process: 
# Create a function to determine the season based on the month and day
# Create a variable to accept user input for the month and day
# Create a mechanism to check the season based on the month and day

def get_season(month, day):
    if month in ["April", "May", "June", "July", "August", "September"]:
        return 'Rainy Season'
    elif month in ["November", "December", "January", "February", "March"]:
        return 'Harmattan (Dry Season)'
    elif month == "October":
        return 'Transition (End of Rainy Season)'
    else:
        return 'Invalid month'

# Input and execution (outside the function!)
month = input("Input the month (e.g. January, February etc.): ").strip().title()  # .title() for consistency
day = int(input("Input the day: "))

season = get_season(month, day)
print(f'Season is {season}')


"""
Question 15: Write a program that asks for the user's name and their favorite color. Then, 
use string interpolation to create a personalized greeting,
"""

#Solution:
#Thought Process:
# Create a variable to accept user input for the name and favorite color
# Use f-string to create a personalized greeting
name = input("Enter your name: ")
favourite_color = input("Enter your favourite color: ")
print(f'Hello {name}, your favourite color is {favourite_color}!')


"""
Question 16: A shop offers a 10% discount if the total bill is over $100. Write a program 
that asks for the total bill amount and prints the final amount to be paid after the 
discount, if applicable.
"""

#Solution:
#Thought Process:
#1. Create a variable to accept user input
#2. create a mechanism to check if the total bill exceed 100
#3. If exceed 100, multiply the discount by total bill, else total bill

enter_amount = int(input("enter total bill amount: "))
discount = 0.1

if enter_amount > 100:
    final_amount = enter_amount - (discount * enter_amount)

    print(f'The total bill amount is {final_amount:.2f}')

else:
    print(f'The total bill amount is {enter_amount:.2f}')


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


"""
Question 18: Create a simple login system. Define a username and password in your 
code. Ask the user to enter their username and password. If they match the 
predefined credentials, print "Login successful." Otherwise, print "Invalid 
credentials."
"""

#Solution:
"""
Thought Process:
- Create a function to validate the username and password
- Use string methods to check for the presence of lowercase, uppercase, digits, and special characters
- Create a variable to accept user input for the password
- Create a mechanism to check the validity of the password based on the given conditions
"""
def validate_credentials(username, password):
    # Username validation
    if len(username) < 6 or len(username) > 16:
        return False
    
    # Password validation
    if len(password) < 8:
        return False
    
    # Character checks
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in {'$', '#', '@'} for char in password)
    
    return has_lower and has_upper and has_digit and has_special

# Input and execution (properly indented). Meaning Proper top-level indentation for the execution block
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if validate_credentials(username, password):
        print(f'CLogin successful')
    else:
        print(f'Invalid credentials')


"""
Question 19: Write a program to determine the price of a movie ticket. 
The base price is $12 for adults (age 18 and over) and $8 for children. 
If it's a weekend, add $2 to the price. Ask the user for their age and if it is a weekend 
(e.g., they can enter 'yes' or 'no').
"""
#Solution:
#Thought Process:
#- Two approach/method can be used to achieve this. A program can be created without a function or a function
#-Create a variable to accept user input

#Method 1:
enter_your_age = int(input("How old are you: "))
is_weekend = input("Yes/No: ").strip().title()
adult_ticket = 12
children_ticket = 8
weekend_price = 2

#Identify the person age and weekend status
if enter_your_age >= 18 and is_weekend == "No":
    print(f'It is a weekday and Adult movie ticket price is {adult_ticket}')

elif enter_your_age < 18 and is_weekend == "No":
    print(f'It is a weekday and Children movie ticket price is {children_ticket}')

elif enter_your_age >= 18 and is_weekend == "Yes":
    total_price = adult_ticket + weekend_price
    print(f'The weekend movie ticket price is {total_price}')

else:
    print(f'The weekend movie ticket price is {children_ticket + weekend_price}')

#Method 2:
#Define a function
def cinema(enter_your_age, is_weekend):
    adult_ticket = 12
    children_ticket = 8
    weekend_price = 2

    #Identify the person age and weekend status
    if enter_your_age >= 18 and is_weekend == "No":
        return f'It is a weekday and Adult movie ticket price is {adult_ticket}'

    elif enter_your_age < 18 and is_weekend == "No":
        return f'It is a weekday and Children movie ticket price is {children_ticket}'

    elif enter_your_age >= 18 and is_weekend == "Yes":
        total_price = adult_ticket + weekend_price
        print(f'The weekend movie ticket price is {total_price}')

    else:
        return f'The weekend movie ticket price is {children_ticket + weekend_price}'

#User Input
enter_your_age = int(input("How old are you: "))
is_weekend = input("Yes/No: ").strip().title()

#Call the function
print(cinema(enter_your_age,is_weekend))


"""
Question 20: Simulate a simple ATM. Initialize a balance, say $1000. 
Ask the user what they want to do: 'withdraw', 'deposit', or 'check balance'. 
If they choose 'withdraw', ask for the amount and subtract it from the balance, 
but only if they have enough funds. If they choose 'deposit', ask for the amount and add it to 
the balance. If they choose 'check balance', display the current balance. 
Handle invalid input gracefully.
"""

#Solution:
#Thought Process:
#Two appraoch can be use. A function or non function
#Create a variable to store the initialize balance
#Create a variable to accept user input of intended action
#Create a mechanism that check the user action type and action by the action type inputted

#Method 1:
def simple_atm(action_type, amount_to_witdraw, deposited_amount):
    action_type = action_type.strip().title()
    initialize_balance = 1000
    
    if action_type == "Withdraw":
        if amount_to_witdraw > 0:
            if amount_to_witdraw <= initialize_balance:
                new_balance = initialize_balance - amount_to_witdraw
                return f'Your balance is {new_balance}'
            else:
                return 'Insufficient funds'
        else:
            return 'Withdrawal amount must be positive'
    
    elif action_type == "Deposit":
        if deposited_amount > 0:
            new_balance = initialize_balance + deposited_amount
            return f'Your balance is {new_balance}'
        else:
            return 'Deposit amount must be positive'
    
    elif action_type == "Check Balance":
        return f'Your balance is {initialize_balance}'
    
    else:
        return 'Invalid action type'

# User input
action_type = input("What do you want to do? (Withdraw/Deposit/Check Balance): ").strip().title()

# Only request relevant amounts
if action_type == "Withdraw":
    amount_to_witdraw = int(input("Enter amount to withdraw: "))
    deposited_amount = 0  # Not used for withdrawal
elif action_type == "Deposit":
    deposited_amount = int(input("Enter the amount to deposit: "))
    amount_to_witdraw = 0  # Not used for deposit
else:  # Check Balance
    amount_to_witdraw = 0
    deposited_amount = 0

print(simple_atm(action_type, amount_to_witdraw, deposited_amount))

#Method 2:
# Initialize balance
initialize_balance = 1000

# Get user input
action_type = input("What do you want to do? (Withdraw/Deposit/Check Balance): ").strip().title()

# Process withdrawal
if action_type == "Withdraw":
    amount_to_withdraw = int(input("Enter amount to withdraw: "))
    if amount_to_withdraw > 0:
        if amount_to_withdraw <= initialize_balance:
            initialize_balance = initialize_balance - amount_to_withdraw
            print(f'Your balance is {initialize_balance}')
        else:
            print('Insufficient funds')
    else:
        print('Withdrawal amount must be positive')

# Process deposit
elif action_type == "Deposit":
    deposited_amount = int(input("Enter the amount to deposit: "))
    if deposited_amount > 0:
        initialize_balance = initialize_balance + deposited_amount
        print(f'Your balance is {initialize_balance}')
    else:
        print('Deposit amount must be positive')

# Check balance
elif action_type == "Check Balance":
    print(f'Your balance is {initialize_balance}')

# Invalid action
else:
    print('Invalid action type')


"""
Question 21: Adventure Game Introduction: Create a very simple text-based adventure 
game. Start with a scenario, e.g., "You are at a crossroads. Do you want to go 'left' or 'right'?" 
Based on the user's choice, present another choice. For example, if they go 'left', they might find 
a 'cave' or a 'river'. Use nested if statements to create a small, branching story with at least two 
levels of choices.
"""

#Solution
#Thought Process:
#Create branching paths with consequences
#Nested if-else statements for decision trees
#2 winning scenarios, multiple failure states

print("Welcome to the Adventure Game!")
print("You find yourself at a mysterious crossroads...\n")

# First choice
choice1 = input("Do you want to go 'left' or 'right'? ").lower()

if choice1 == "left":
    print("\nYou chose the left path and find yourself by a dark cave.")
    print("A faint light glows from within.\n")
    
    # Second level choice for left path
    choice2 = input("Do you want to 'enter' the cave or 'continue' along the path? ").lower()
    
    if choice2 == "enter":
        print("\nYou discover a treasure chest inside the cave!")
        print("Congratulations! You win!")
    elif choice2 == "continue":
        print("\nYou walk further and fall into a hidden pit.")
        print("Game Over!")
    else:
        print("\nYou hesitated too long and a wild bear attacks you!")
        print("Game Over!")

elif choice1 == "right":
    print("\nYou chose the right path and come to a rushing river.")
    print("The water looks deep and dangerous.\n")
    
    # Second level choice for right path
    choice2 = input("Do you want to 'swim' across or 'build' a raft? ").lower()
    
    if choice2 == "swim":
        print("\nThe current is too strong! You get swept away.")
        print("Game Over!")
    elif choice2 == "build":
        print("\nYou safely cross the river and find a friendly village.")
        print("Congratulations! You win!")
    else:
        print("\nWhile you were deciding, night fell and wolves attacked!")
        print("Game Over!")

else:
    print("\nYou couldn't decide which way to go and got lost in the woods.")
    print("Game Over!")