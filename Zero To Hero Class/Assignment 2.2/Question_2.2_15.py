#Write a Python program to access a function inside a function.
#Solution:
#Thought Process:
#Create a function that accepts a number
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# Get user input as a tuple of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Call the function and unpack the results
even_count, odd_count = count_even_odd(numbers)
# Print the results
print(f'Total even numbers: {even_count}')
print(f'Total odd numbers: {odd_count}')