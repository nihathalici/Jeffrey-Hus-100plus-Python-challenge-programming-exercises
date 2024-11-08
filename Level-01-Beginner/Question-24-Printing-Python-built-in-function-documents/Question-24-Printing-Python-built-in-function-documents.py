"""
Question 24

Level 1

Question:

Python has many built-in functions, and if you do not know how to use it, you can read 
document online or find some books. But Python has a built-in document function for every 
built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), 
int(), input()

And add document for your own function Hints: The built-in document method is doc

Solution:
"""

print("Below is the document of abs: ")
print(abs.__doc__)
print("-------------------------------")
print("Below is the document of int: ")
print(int.__doc__)
print("-------------------------------")
print("Below is the document of input: ")
print(input.__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print("-------------------------------")
print("Below is the document of square function: ")
print(square.__doc__)