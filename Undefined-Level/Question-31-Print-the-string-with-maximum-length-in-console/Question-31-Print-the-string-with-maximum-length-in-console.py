""" 
Question 31

Define a function that can accept two strings as input and print the string with maximum 
length in console. If two strings have the same length, then the function should print all 
strings line by line.

Hints:

Use len() function to get the length of a string

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:
"""

def print_val(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len2 > len1:
        print(s2)
    else:
        print(s1 + "\n" + s2)

# Prints out:
# one
# tre        
print_val("one","tre") 

