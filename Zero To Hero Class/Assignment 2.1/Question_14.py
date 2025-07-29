"""
Question 14: Write a Python program that reads two integers representing a month and 
day and prints the season for that month and day. 
Expected Output: 
Input the month (e.g. January, February etc.): july                      
Input the day: 31                                                        
Season is harmattan
"""

#Solution:
#Thought Process: 
# Create a function to determine the season based on the month and day
# Create a variable to accept user input for the month and day
# Create a mechanism to check the season based on the month and day
# Wrap the logic using error handling mechanism

def get_season(month, day):
    if month in ["April", "May", "June", "July", "August", "September"]:
        return 'Rainy Season'
    elif month in ["November", "December", "January", "February", "March"]:
        return 'Harmattan (Dry Season)'
    elif month == "October":
        return 'Transition (End of Rainy Season)'
    else:
        return 'Invalid month'

#Handle Error
try:
    # Input and execution (outside the function!)
    month = input("Input the month (e.g. January, February etc.): ").strip().title()  # .title() for consistency
    day = int(input("Input the day: "))
    
    season = get_season(month, day)
    print(f'Season is {season}')

except TypeError:
    print(f'Please enter a month correctly. ')
