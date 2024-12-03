""" 
Define a function that can accept an integer number as input and print the 
"It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.


Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:
"""
def check_value(n):
    if n % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
check_value(7)
