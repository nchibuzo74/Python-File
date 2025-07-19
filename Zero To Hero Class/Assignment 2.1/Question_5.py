"""
Question 5: Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

#Solution:
"""
Thought Process: The area of a circle is pi r square (r^2)
- Create a variable to accept the radius inputted by the user
- Let pie be 3.142
"""
pie = 3.142
radius = float(input("Enter the radius: "))
area = ((pie) * (radius * radius))

print(f'The area of a circle is {area}')
