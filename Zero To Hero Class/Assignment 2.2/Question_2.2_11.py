"""
Write a Python program to calculate a dog's age in dog years. 
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year 
equals 4 human years.
"""

#Solution:
#Thought Process:
#Create a variable that accept user input of the dog's age
#Create a mechanism to calculate the dog's age in dog years
dog_age = float(input("Enter the dog's age in human years: "))
# Calculate dog's age in dog years
if dog_age <= 2:
    dog_years = dog_age * 10.5
else:
    dog_years = 21 + (dog_age - 2) * 4
print(f"The dog's age in dog years is: {dog_years}")
