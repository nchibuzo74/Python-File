#Create a Calculator that does Addition, Subtraction, Multiplication and Division.

#Solution:
#Thought process:
#Create a several functions to house the logic
#Create a variable asking user of the action type
#Create a variable accepting user inputs

def calculator():
    print("Welcome to Simple Calculator!")
    print("Available operations: Addition, Subtraction, Multiplication, Division")
    
    # Accepting user input for the action type
    action_type = input("What do you intend to do?: ").strip().title()
    
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
    except ValueError:
        return "Error: Please enter valid integers!"

    # Performing the action based on user input
    if action_type == "Addition":
        return Add_Function(first_number, second_number)
    elif action_type == "Subtraction":
        return Subt_Function(first_number, second_number)
    elif action_type == "Multiplication":
        return Mult_Function(first_number, second_number)
    elif action_type == "Division":
        return Div_Function(first_number, second_number)
    else:
        return "Invalid operation selected"

def Add_Function(first_number, second_number):
    result_add = first_number + second_number
    return f'Addition of the two numbers is {result_add}'

def Subt_Function(first_number, second_number):
    result_subt = first_number - second_number
    return f'Subtraction of the two numbers is {result_subt}'

def Mult_Function(first_number, second_number):
    result_mult = first_number * second_number
    return f'Multiplication of the two numbers is {result_mult}'

def Div_Function(first_number, second_number):
    if second_number == 0:  # Only need to check for division by zero
        return 'Error: Cannot divide by zero!'
    result_div = first_number / second_number
    return f'Division of the two numbers is {result_div}'

# Run the calculator
print(calculator())