#5. Write a program that repeatedly asks the user for a number until they enter 0. After they enter 0, 
# print the sum of all the numbers they entered (excluding the 0).

#Solution:
#Thought Process:
#Create a variable to accept users input
#Create a mechanism to identity the number from the user input if it's zero or not
#If enter zero, sum up all the numbers they entered before excluding zero
#Wrap the logic using error handling mechanism

total = 0

while True:
    user_input = input("Enter a number (0 to stop): ")
    try:
        num = float(user_input)
    except ValueError:
        print("Please enter a valid number")
        continue
    
    if num == 0:
        break
    total = total + num

print(f"The sum is: {total}")