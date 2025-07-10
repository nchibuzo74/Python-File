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
