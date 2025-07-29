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
- Wrap the logic using error handling mechanism
"""

#Handle Error
try:
    Principal = int(input("Enter the Principal amount: "))
    Rate = int(input("Enter the Rate (%): "))
    Time = int(input("Enter the Time (in years): "))
    
    SI = (Principal * Rate * Time) / 100
    
    print(f'The Simple Interest is {SI}')

except ValueError:
    print(f'Please enter a number correctly. ')

finally:
    print(f'Thanks for complying. ')
