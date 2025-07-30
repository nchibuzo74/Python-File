#7. Write a Python program to get the Fibonacci series between 0 and 50.

#Solution:
#Thought Process:
#Create a loop to generate Fibonacci numbers
#Continue until the numbers exceed 50
#Wrap the logic using error handling mechanism

def fibonacci_series(limit):
    fib_series = []
    a, b = 0, 1

    # Handle Error
    try:
        while a <= limit:
            fib_series.append(a)
            a, b = b, a + b
        return fib_series  # Moved outside the while loop
    except ValueError:
        print('Please enter a number correctly.')
        return []  # Return empty list on error
    finally:
        print('Thank you.')
        
fib_numbers = fibonacci_series(50)
print("Fibonacci series between 0 and 50:", fib_numbers)
