"""
Question 4: Prompt the user to enter their score and:
print grade A (90-100), B (80-89), C (70-79), F (below 70)
"""

#Solution:
"""
Thought Process: 
i. Create a variable to allow users to input
ii. Create a mechanism to identify their grade
"""
Score = int(input("Enter your score: "))

if Score >= 90 and Score <= 100:
    print(f'Grade A')

elif Score >= 80 and Score <= 89:
    print(f'Grade B')

elif Score >= 70 and Score <= 79:
    print(f'Grade C')

else:
    print(f'Grade F')
