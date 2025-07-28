#In a range of 1 to 6, there are even numbers. Print the numbers when the number is 5.

#Solution:
#Let the numbers be number
number = []

#Let the new variable be num
for num in range(1,6):
    if num % 2 == 0:
        continue #skip the even numbers
    if num == 5:
        break #stop the loop
    #number.append(num)
    #print(f'numbers are: {num}')

#Function exercise
#Question: Write a program to create a function that takes two arguments, name and age and prints their values.
def sample(name_,age):
    print(name_,age)
    
#Object
#sample("Chibuzo",30)

################################
x = 5

if x > 2:
    #continue #skip 3,4,5

    if x < 4:
        print("Low")

    elif x == 5:
        print("Exact")


########################
def func(a, L=[]):
    for i in range(a):
        L.append(i)
    return L

print(func(2))
print(func(3))


def get_season(month, day):
    if month in ["April", "May", "June", "July", "August", "September"]:
        return "Rainy Season"
    elif month in ["November", "December", "January", "February", "March"]:
        return "Harmattan (Dry Season)"
    elif month == "October":
        return "Transition (End of Rainy Season)"
    else:
        return "Invalid month"

# Input month and day
month = input("Input the month (e.g. January, February etc.): ").strip()
day = int(input("Input the day: "))
# Get and print the season
season = get_season(month, day)
print(f"Season is {season}")

