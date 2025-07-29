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
# Wrap the logic using error handling mechanism

#Method 1:
# Global balance variable to persist across function calls
balance = 1000

def simple_atm(action_type, amount=0):
    global balance
    action_type = action_type.strip().title()
    
    if action_type == "Withdraw":
        if amount > 0:
            if amount <= balance:
                balance = balance - amount
                return f'Withdrawal successful. Your balance is ${balance}'
            else:
                return 'Insufficient funds'
        else:
            return 'Withdrawal amount must be positive'
    
    elif action_type == "Deposit":
        if amount > 0:
            balance = balance + amount
            return f'Deposit successful. Your balance is ${balance}'
        else:
            return 'Deposit amount must be positive'
    
    elif action_type == "Check Balance":
        return f'Your balance is ${balance}'
    
    else:
        return 'Invalid action type'

# User input
action_type = input("What do you want to do? (Withdraw/Deposit/Check Balance): ").strip().title()

# Handle Error
try:
    if action_type == "Withdraw":
        amount = int(input("Enter amount to withdraw: "))
        result = simple_atm(action_type, amount)
        print(result)
        
    elif action_type == "Deposit":
        amount = int(input("Enter the amount to deposit: "))
        result = simple_atm(action_type, amount)
        print(result)
        
    elif action_type == "Check Balance":
        result = simple_atm(action_type)
        print(result)
        
    else:
        print('Invalid action type')

except ValueError:
    print('Please enter a valid amount.')

finally:
    print('Thank you for using the ATM service!')


################################################################################################################################################
#Method 2:
# Initialize balance
initialize_balance = 1000

# Get user input
action_type = input("What do you want to do? (Withdraw/Deposit/Check Balance): ").strip().title()

# Handle Error
try:
    # Process withdrawal
    if action_type == "Withdraw":
        amount_to_withdraw = int(input("Enter amount to withdraw: "))
        if amount_to_withdraw > 0:
            if amount_to_withdraw <= initialize_balance:
                initialize_balance = initialize_balance - amount_to_withdraw
                print(f'Withdrawal successful. Your balance is ${initialize_balance}')
            else:
                print('Insufficient funds')
        else:
            print('Withdrawal amount must be positive')
            
    # Process deposit
    elif action_type == "Deposit":
        deposited_amount = int(input("Enter the amount to deposit: "))
        if deposited_amount > 0:
            initialize_balance = initialize_balance + deposited_amount
            print(f'Deposit successful. Your balance is ${initialize_balance}')
        else:
            print('Deposit amount must be positive')
            
    # Check balance
    elif action_type == "Check Balance":
        print(f'Your balance is ${initialize_balance}')
        
    # Invalid action
    else:
        print('Invalid action type')

except ValueError:
    print('Please enter a valid amount.')

finally:
    print('Thank you for using the ATM service!')