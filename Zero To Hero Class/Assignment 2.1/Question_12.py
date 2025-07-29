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
- Wrap the logic using error handling mechanism
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

#Handle Error
try:
    if validate_password(password):
        print("Password is valid!")
    else:
        print("Password is invalid!")

except TypeError:
    print(f'Please enter an valid password. ')

finally:
    print(f'Thanks for complying. ')
