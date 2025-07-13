#Create a Calculator that does Addition, Subtraction, Multiplication and Division.

#Solution:
#Thought process:
#Create a several functions to house the logic
#Create a variable asking user of the action type
#Create a variable accepting user inputs

def calculator():
    print("Welcome to Simple Calculator!")
    print("Available operations: Addition, Subtraction, Multiplication, Division")

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
    if first_number >= 0 and second_number > 0:
        result_div = first_number / second_number
        return f'Division of the two numbers is {result_div}'

    else:
        return f'Error: Try again'

#Object
print(calculator())
#Strip() and Title() is use to convert the text to first letter to be capital letter while the rest small letter
action_type = input("What do you intend to do?: ").strip().title()

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if action_type == "Addition":
    print(Add_Function(first_number, second_number))

elif action_type == "Subtraction":
    print(Subt_Function(first_number, second_number))

elif action_type == "Multiplication":
    print(Mult_Function(first_number, second_number))

elif action_type == "Division":
    print(Div_Function(first_number, second_number))

else:
    print(f'Invalid operation selected')