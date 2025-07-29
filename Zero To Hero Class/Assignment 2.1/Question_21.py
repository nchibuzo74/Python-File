"""
Question 21: Adventure Game Introduction: Create a very simple text-based adventure 
game. Start with a scenario, e.g., "You are at a crossroads. Do you want to go 'left' or 'right'?" 
Based on the user's choice, present another choice. For example, if they go 'left', they might find 
a 'cave' or a 'river'. Use nested if statements to create a small, branching story with at least two 
levels of choices.
"""

#Solution
#Thought Process:
#Create branching paths with consequences
#Nested if-else statements for decision trees
#2 winning scenarios, multiple failure states
# Wrap the logic using error handling mechanism

print("Welcome to the Adventure Game!")
print("You find yourself at a mysterious crossroads...\n")

#Handle Error
try:
    # Start of the adventure
    print("You can go 'left' or 'right'. Choose wisely!")
    
    # First choice
    choice1 = input("Do you want to go 'left' or 'right'? ").lower()
    
    if choice1 == "left":
        print("\nYou chose the left path and find yourself by a dark cave.")
        print("A faint light glows from within.\n")
        
        # Second level choice for left path
        choice2 = input("Do you want to 'enter' the cave or 'continue' along the path? ").lower()
        
        if choice2 == "enter":
            print("\nYou discover a treasure chest inside the cave!")
            print("Congratulations! You win!")
            
        elif choice2 == "continue":
            print("\nYou walk further and fall into a hidden pit.")
            print("Game Over!")
            
        else:
            print("\nYou hesitated too long and a wild bear attacks you!")
            print("Game Over!")
            
    elif choice1 == "right":
        print("\nYou chose the right path and come to a rushing river.")
        print("The water looks deep and dangerous.\n")
        
        # Second level choice for right path
        choice2 = input("Do you want to 'swim' across or 'build' a raft? ").lower()
        
        if choice2 == "swim":
            print("\nThe current is too strong! You get swept away.")
            print("Game Over!")
        elif choice2 == "build":
            print("\nYou safely cross the river and find a friendly village.")
            print("Congratulations! You win!")
            
        else:
            print("\nWhile you were deciding, night fell and wolves attacked!")
            print("Game Over!")
            
    else:
        print("\nYou couldn't decide which way to go and got lost in the woods.")
        print("Game Over!")

except ValueError:
    print("Please enter a valid choice (left/right, enter/continue, swim/build).")

# Final message
finally:
    print("Thank you for playing the Adventure Game! Hope you enjoyed it!")