"""
Question 19: Write a program to determine the price of a movie ticket. 
The base price is $12 for adults (age 18 and over) and $8 for children. 
If it's a weekend, add $2 to the price. Ask the user for their age and if it is a weekend 
(e.g., they can enter 'yes' or 'no').
"""
#Solution:
#Thought Process:
# Two approach/method can be used to achieve this. A program can be created without a function or a function
# Create a variable to accept user input
# Wrap the logic using error handling mechanism

#Method 1:
enter_your_age = int(input("How old are you: "))
is_weekend = input("Yes/No: ").strip().title()
adult_ticket = 12
children_ticket = 8
weekend_price = 2

#Handle Error
try:
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

except ValueError:
    print(f'Please enter a number correctly. ')


#########################################################################################################################################
#Method 2:
#Define a function
def cinema(enter_your_age, is_weekend):
    adult_ticket = 12
    children_ticket = 8
    weekend_price = 2

    # Identify the person age and weekend status
    if enter_your_age >= 18 and is_weekend == "No":
        return f'It is a weekday and Adult movie ticket price is ${adult_ticket}'

    elif enter_your_age < 18 and is_weekend == "No":
        return f'It is a weekday and Children movie ticket price is ${children_ticket}'

    elif enter_your_age >= 18 and is_weekend == "Yes":
        total_price = adult_ticket + weekend_price
        return f'It is a weekend and Adult movie ticket price is ${total_price}'

    else:  # Child on weekend
        total_price = children_ticket + weekend_price
        return f'It is a weekend and Children movie ticket price is ${total_price}'

# Handle Error
try:
    # User Input
    enter_your_age = int(input("How old are you: "))
    is_weekend = input("Is it weekend? (Yes/No): ").strip().title()
    
    # Validate weekend input
    if is_weekend not in ["Yes", "No"]:
        print("Please enter 'Yes' or 'No' for weekend status.")
    else:
        # Call the function
        result = cinema(enter_your_age, is_weekend)
        print(result)

except ValueError:
    print('Please enter correct information.')

finally:
    print('Thank you for complying.')