""" 
Question 34

Define a function which can print a dictionary where the keys are numbers between 1 and 20 
(both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number. Use range() for loops.


Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:
"""

def print_squares():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	print(d)

print_squares()


"""
Alternative Solution:
"""

def print_squares():
    squares = {i: i**2 for i in range(1, 21)}
    print(squares)
