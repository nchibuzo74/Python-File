"""
Write a Python function that takes a number as a parameter and checks whether the 
number is prime or not. 
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive 
divisors other than 1 and itself.
"""

#Solution:
#Thought Process:
#Create a function that accepts a number
#Check if the number is less than 2, if so, it is not prime
#Wrap the logic using error handling mechanism

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Handle Error
try:
    # Get user input
    number = int(input("Enter a number: "))
    
    # Check if the number is prime
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        
except ValueError:
    print("Please enter a valid integer.")

# Finally block to ensure the program ends gracefully
finally:
    print("Thank you for using the prime number checker!")