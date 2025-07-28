#List
list_of_items = ["apple","banana","cheery"]
#print(list_of_items)

#Dictionary
dictionary_items = {"name": ["Ade","Eze","Bruno"],
                     "Age": [20,30,50]}

#print(dictionary_items)

#Membership operator
name = "Chibuzo"

#print("i" in name)

#If statement
#height = float(input("Enter your height: "))
#print(height)


#Write a python to calculate the BMI of a person
#Solution:
#My thought process: create variables to capture the following - 
# identify the age, height and weight of the person

age = int(input("How old are you: "))
height = float(input("Enter your height in CM: "))
weight = float(input("Enter your weight in KG: "))

height_m = height / 100
bmi = round((weight / height_m),2)

if bmi < 16:
    print(f'Your age: {age} and BMI: {bmi}. You are Very Severely Underweight')

elif bmi >= 16 and bmi <= 17:
    print(f'Your age: {age} and BMI: {bmi}. You are Severely Underweight')

elif bmi > 17 and bmi <= 18.5:
    print(f'Your age: {age} and BMI: {bmi}. You are Underweight')

elif bmi > 18.5 and bmi <= 25:
    print(f'Your age: {age} and BMI: {bmi}. You are Normal')

elif bmi > 25 and bmi <= 30:
    print(f'Your age: {age} and BMI: {bmi}. You are Overweight')

elif bmi > 30 and bmi <= 35:
    print(f'Your age: {age} and BMI: {bmi}. You are Obese Class I')

elif bmi > 35 and bmi <= 40:
    print(f'Your age: {age} and BMI: {bmi}. You are Obese Class II')

else:
    print(f'Your age: {age} and BMI: {bmi}. You are Obese Class III')
