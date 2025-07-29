"""
Question 4: Prompt the user to enter their score and:
print grade A (90-100), B (80-89), C (70-79), F (below 70)
"""

#Solution:
"""
Thought Process: 
i. Create a variable to allow users to input
ii. Create a mechanism to identify their grade
iii.Wrap the logic using error handling mechanism
"""
#Handles errors
try:
    score = int(input("Enter your score: "))
    
    if score >= 90 and score <= 100:
        print('Grade A')
    elif score >= 80 and score <= 89:
        print('Grade B')
    elif score >= 70 and score <= 79:
        print('Grade C')
    elif score < 70:
        print('Grade F')
    else:
        print('Invalid score. Please enter a score between 0-100.')
        
except ValueError:
    print('Please enter a valid number. ')
        
