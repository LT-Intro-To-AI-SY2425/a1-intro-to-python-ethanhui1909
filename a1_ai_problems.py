# Complete your individualized AI problems here
'''
1. Palindrome Checker
Problem: Write a function is_palindrome that checks if a given string is a palindrome. 
A palindrome is a word or phrase that reads the same backward as forward (e.g., "madam", "racecar"). Your function should ignore spaces, punctuation, and case differences.

2. Fibonacci Sequence Generator
Problem: Write a function fibonacci_sequence that generates the first n numbers in the Fibonacci sequence. 
The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

3. Basic Calculator
Problem: Write a simple calculator function calculate that takes a string representing a mathematical expression and evaluates it. 
The string will consist of two operands and one operator (e.g., "3 + 4"). Implement basic operations such as addition, subtraction, multiplication, and division.
'''

def palindrome(input_string: str) -> bool:
    x = input_string[::-1]
    return x==input_string

def fibonacci(input_int: int) -> list:
    if input_int <= 0:
        return []
    elif input_int == 1:
        return [0]
    elif input_int == 2:
        return [0, 1]

    x = [0, 1]
    for i in range(2, input_int):
        x.append(x[i - 1] + x[i - 2])
    
    return x

def calculator(num1: int, num2: int, operator: str) -> int:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 // num2  # Use // for integer division
    else:
        raise ValueError("Invalid operator. Use +, -, *, or /.")

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

