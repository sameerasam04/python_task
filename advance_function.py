#task1
"""Write a Python function square_all(numbers) that takes a list of numbers as input
and returns a new list containing the square of each number in the input list.
Use the map() function with a lambda function to implement this."""
list_1 = [21,92,83,41,53,]
def square_all(i):
    return list(map(lambda i:i ** 2,list_1))
squared_numbers = square_all([21,92,83,41,53])
print(squared_numbers)

#task2
"""Write a Python function filter_positive(numbers) that takes a list of numbers as
input and returns a new list containing only the positive numbers from the
input list. Use the filter() function with a lambda function to implement this."""

list_1 = [12,13,14,15,16,18,19,20,21]
def filter_positive(i):
    return list(filter(lambda i: i > 0,list_1))

input_numbers = [-20,-15, 0, 15, 20]
positive_numbers = filter_positive(input_numbers)
print(positive_numbers) 



#task3
"""Write a Python function calculate_factorial(n) that calculates the factorial of a
given number n . Use the reduce() function with an appropriate lambda
function to implement this."""

def factorial(n):
    factorial = 1  
    for i in range(1, n + 1):
        factorial *= i  
    return factorial  

n = int(input("Enter an integer: "))
print("Factorial of", n, "is", factorial(n))

from functools import reduce

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda i, n: n * 1, range(1, n + 1))

factorial_of_5 = calculate_factorial(5)
print(factorial_of_5)  

#task4
"""Write a Python function count_vowels(string) that takes a string as input and
returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce()
function with an appropriate lambda function to implement this."""

from functools import reduce

def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return reduce(lambda count, char: count + (1 if char in vowels else 0), string, 0)

input_string = "Hello, how are you?"
vowel_count = sum(1 for char in input_string if char.lower() in "aeiou")
print(vowel_count)