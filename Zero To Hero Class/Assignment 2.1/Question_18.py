"""
Question 18: Create a simple login system. Define a username and password in your 
code. Ask the user to enter their username and password. If they match the 
predefined credentials, print "Login successful." Otherwise, print "Invalid 
credentials."
"""

#Solution:
"""
Thought Process:
- Create a function to validate the username and password
- Use string methods to check for the presence of lowercase, uppercase, digits, and special characters
- Create a variable to accept user input for the password
- Create a mechanism to check the validity of the password based on the given conditions
- Wrap the logic using error handling mechanism
"""
def validate_credentials(username, password):
    # Username validation
    if len(username) < 6 or len(username) > 16:
        return False
    
    # Password validation
    if len(password) < 8:
        return False
    
    # Character checks
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in {'$', '#', '@'} for char in password)
    
    return has_lower and has_upper and has_digit and has_special

# Input and execution (properly indented). Meaning Proper top-level indentation for the execution block
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

#Handle Error
try:
    if validate_credentials(username, password):
        print(f'Login successful')
    else:
        print(f'Invalid credentials')

except TypeError:
    print(f'Please a correct username and password. ')

#Greetings
finally:
    print(f'Thanks for complying. ')