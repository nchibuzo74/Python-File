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
