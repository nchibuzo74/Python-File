#7. Write a Python program to get the Fibonacci series between 0 and 50.

#Solution:
#Thought Process:
#Create a loop to generate Fibonacci numbers
#Continue until the numbers exceed 50
def fibonacci_series(limit):
    fib_series = []
    a, b = 0, 1
    while a <= limit:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
fib_numbers = fibonacci_series(50)
print("Fibonacci series between 0 and 50:", fib_numbers)
