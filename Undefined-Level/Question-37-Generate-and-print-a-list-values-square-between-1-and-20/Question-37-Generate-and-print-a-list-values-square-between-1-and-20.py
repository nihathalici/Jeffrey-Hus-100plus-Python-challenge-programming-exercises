""" 
Question 37

Define a function which can generate and print a list where the values 
are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() 
to add values into a list.

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:
"""
def print_list():
	li = list()
	for i in range(1, 21):
		li.append(i ** 2)
	print(li)

print_list()

"""
1. Alternative Solution:
"""

def print_list():
    li = []
    for i in range(1, 21):
        li.append(i ** 2)
    print(li)


"""
2. Alternative Solution:
"""

def print_list():
    li = [i ** 2 for i in range(1, 21)]
    print(li)

"""
3. Alternative Solution:
"""

def print_list():
    print([i ** 2 for i in range(1, 21)])


