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
iii. Wrap the logic using error handling mechanism
"""
#Handles errors
try:
    Quantity = int(input("Enter the quantity bought: "))
    Price = int(input("Enter the sales amount of the product: "))
    
    #Calculate the bill
    total_bill = Quantity * Price
    print(f'The customer total bill is {total_bill}')

except ValueError:
    print(f'Please enter the quantity and price correctly.')