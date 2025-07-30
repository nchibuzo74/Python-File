"""
1.Write a Python program to construct the following pattern, using a nested for loop. 
*  
* *  
* * *  
* * * *  
* * * * *  
* * * *  
* * *  
* *  
* 
"""

#Solution:
#Thought Process: 
# Create a varaible to store the list of stars in memory
# Use a for statement to loop the increasing stars within the range of stars
#Print the stars
#Loop again with the for statement to loop the decreasing stars within the range of stars
#Print the stars
#Wrap the logic using error handling mechanism

#Handle Error
try:
    # Number of rows in the upper half of the pattern
    n = 5
    
    # Upper half (increasing stars)
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()  # Move to the next line after printing all stars in the row
            
    # Lower half (decreasing stars)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()  # Move to the next line after printing all stars in the row

except ValueError:
    print(f'Please enter a number correctly. ')

finally:
    print(f'Thank you for using the program!')