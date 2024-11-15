# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KUhtcrNALfREYdn05IqcLvjKjzruja5
"""

# 1.1 Insert the missing indentation to make the code correct
if 4 == 2:
    print("Four is equal to two!")

# 1.2 Variables

# 1.2.1 Create a variable named fruit and assign the value Apple to it.
fruit = "Apple"

# 1.2.2 Create a variable called z, assign x + y to it, and display the result.
x = 10
y = 20

# TODO: Write your code below
z = x + y
print(z)

# 1.2.3 Remove the illegal characters in the variable name:
city_name = "London"

# 1.2.4 Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
    global x
    x = "fantastic"

# 1.2.5 Write a program that switches the values stored in variables a and b.
a = 5
b = 4

# Swapping values
a, b = b, a

print('a :', a)
print('b :', b)

# 1.3 Data Types

# 1.3.1 Write a program that adds the digits in a two-digit number input.
# eg. if the input is 45, the output should be 4 + 5 = 9
number = input("Enter a two-digit number: ")

# Split digits and sum
digit_sum = int(number[0]) + int(number[1])
print("The sum of the digits is:", digit_sum)
# 2.1 Strings
# HINT: https://www.w3schools.com/python/python_strings.asp

txt = "Merry Christmas"

# 2.1.1 Print the length of the string
# TODO: Write your code below
print(len(txt))

# 2.1.2 Print the first character of the string txt.
# TODO: Write your code below
print(txt[0])

# 2.1.3 Get the characters from index 1 to index 3 ("err").
# TODO: Write your code below
print(txt[1:4])

# 2.1.4 Convert the value of txt to upper case and print it.
# TODO: Write your code below
print(txt.upper())

# 2.1.5 Convert the value of txt to lower case and print it.
# TODO: Write your code below
print(txt.lower())

# 2.1.6 Return the string without any whitespace at the beginning or the end.
x = " Hello World "
# TODO: Write your code below
print(x.strip())

# 2.1.7 Replace the character H with a J and print the result
y = "Hello"
# TODO: Write your code below
print(y.replace("H", "J"))

# 2.1.8 Insert the correct syntax to add a placeholder for the name parameter.
# TODO: Update the code below
name = 'John'
txt = "My name is {}"
print(txt.format(name))
# 3.1 Operators

# 3.1.1 Multiply 4 with 8, and print the result.
# TODO: Write your code below
print(4 * 8)

# 3.1.2 Divide 30 by 6, and print the result.
# TODO: Write your code below
print(30 / 6)
# 4.1 PYTHON Lists

fruits = ["kiwi", "pineapple", "apple"]

# 4.1.1 Print the second item in the fruits list.
# TODO: Write your code below
print(fruits[1])

# 4.1.2 Change the value from "kiwi" to "orange" in the fruits list.
# TODO: Write your code below
fruits[0] = "orange"

# 4.1.3 Use the insert method to add "lemon" as the second item in the fruits list.
# TODO: Write your code below
fruits.insert(1, "lemon")

# 4.1.4 Use the remove method to remove "pineapple" from the fruits list.
# TODO: Write your code below
fruits.remove("pineapple")

# 4.1.5 Use negative indexing to print the last item in the list.
# TODO: Write your code below
print(fruits[-1])

# 4.1.6 Use a range of indexes to print the third, fourth, and fifth item in the list fruits2.
fruits2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# TODO: Write your code below
print(fruits2[2:5])

# 4.1.7 Use the correct syntax to print the number of items in the list fruits.
# TODO: Write your code below
print(len(fruits))

# 4.1.8 Write a program that calculates and prints the average of numbers in a list scores.
# You are not allowed to use the sum() or len() functions.
scores = [50, 55, 56, 70, 80, 60, 66]
# TODO: Write your code below
total = 0
count = 0
for score in scores:
    total += score
    count += 1
average = total / count
print("Average:", average)

# 4.1.9 Write a program that calculates the largest number in a list scores.
# You are not allowed to use the max or min functions.
scores = [50, 55, 56, 70, 80, 60, 66]
# TODO: Write your code below
largest = scores[0]
for score in scores:
    if score > largest:
        largest = score
print("Largest number:", largest)

# 4.2. PYTHON Dictionaries

car = {"brand": "Renault", "model": "Clio","year": 2018}

# 4.2.1 Use the get method to print the value of the "model" key of the car dictionary.
# TODO: Write your code below
print(car.get("model"))

# 4.2.2 Change the "year" value from 2018 to 2020 in the car dictionary.
# TODO: Write your code below
car["year"] = 2020

# 4.2.3 Add the key/value pair "color": "blue" to the car dictionary.
# TODO: Write your code below
car["color"] = "blue"

# 4.2.4 Use the pop method to remove "model" from the car dictionary.
# TODO: Write your code below
car.pop("model")

# 4.2.5 Use the clear method to empty the car dictionary.
# TODO: Write your code below
car.clear()
# 5.1 If ... else

a = 20
b = 40

c = 10
d = 40

# 5.1.1 Print "Yes" if a is equal to b, otherwise print "No".
# TODO: Write your code below
if a == b:
    print("Yes")
else:
    print("No")

# 5.1.2 Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
# TODO: Write your code below
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

# 5.1.3 Print "Hello" if a is equal to b, and c is equal to d.
# TODO: Write your code below
if a == b and c == d:
    print("Hello")

# 5.1.4 Print "Hello" if a is equal to b, or if c is equal to d.
# TODO: Write your code below
if a == b or c == d:
    print("Hello")

# 5.2 Write a program that checks whether an input number is odd or even.
# Print whether the input number is odd or even

# number to check
number = int(input('Enter a number: '))

# TODO: write your code below
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
# 6.1 For Loops

fruits = ["kiwi", "banana", "cherry"]

# 6.1.1 Use a for loop to loop through the items in the fruits list and print each item.
# TODO: Write your code below
for fruit in fruits:
    print(fruit)

# 6.1.2 In the for loop to loop through the items in the fruits list, when the item value is "banana", jump directly to the next item.
# TODO: Write your code below
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# 6.1.3 In the for loop to loop through the items in the fruits list, exit the loop when the item is "banana".
# TODO: Write your code below
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# 6.1.4 Using the Python range() function, create a sequence of numbers from 0 to 5, and print each item in the sequence in a new line.
# TODO: Write your code below
for number in range(6):
    print(number)
# 7.1.3 Create a function named function2 that takes in one integer parameter number1. The function adds 5 to the input number1, and prints the result
# TODO: Write your code below
def function2(number1):
    result = number1 + 5
    print(result)

# 7.1.4 Create a function named compare_numbers() with two arguments. If the first argument is greater than the second, print "first number is greater".
# If the second number is greater than the first, print "first number is smaller". If the numbers are equal, print "equal numbers"
# TODO: Write your code below
def compare_numbers(num1, num2):
    if num1 > num2:
        print("first number is greater")
    elif num1 < num2:
        print("first number is smaller")
    else:
        print("equal numbers")

# 7.2 Create a lambda function that takes one parameter (a) and returns it.
# TODO: Write your code below
lambda_function = lambda a: a
print(lambda_function(5))  # Example of using the lambda function

### 7.3 Python built-in functions :

nums = [11, 33, 14, 2, 58, 65, 34]

# 7.3.1 Using Python's built in sum() function, print the sum of the numbers in the list nums
# TODO: Write your code below
print(sum(nums))

# 7.3.2 Using Python's built in min() function, print the minimum of the numbers in the list nums
# TODO: Write your code below
print(min(nums))

# 7.3.3 Using Python's built in abs() function, print the absolute value of -6.
# TODO: Write your code below
print(abs(-6))

# 7.3.4 Using Python's built in round() function, round the number 4.67888 to two decimal places.
# TODO: Write your code below
print(round(4.67888, 2))

# 7.4 Python Modules

# 7.4.1 Create a python module mod.
# Create mod.py file:

# mod.py
def psum(number1, number2):
    print(number1 + number2)

def pmultiply(number1, number2):
    print(number1 * number2)


# 7.4.2 Create python file main.py and import the module mod.
# In main.py run the psum() and pmultiply() functions from the module mod using any two numbers.

# main.py
import mod

mod.psum(10, 20)
mod.pmultiply(10, 20)

# 7.4.3 In main.py, also import Python's built-in module platform. Then list the functions and variables in the platform module using the dir() function.

# main.py (continued)
import platform

print(dir(platform))