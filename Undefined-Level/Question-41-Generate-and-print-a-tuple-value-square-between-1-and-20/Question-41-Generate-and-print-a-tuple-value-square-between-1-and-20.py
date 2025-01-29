"""
Question 41

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list. Use tuple() to get a tuple from a list

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:
"""

def generate_squares_tuple():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(tuple(li))

generate_squares_tuple()

 
"""
Alternative Solution-1
"""

def generate_squares_tuple():
    squares_list = []
    for num in range(1, 21):
        sq = num ** 2
        squares_list.append(sq)
    squares_tuple = tuple(squares_list)
    print(squares_tuple)

generate_squares_tuple()


"""
Alternative Solution-2
"""

def generate_squares_tuple():
    squares_tuple = tuple(num ** 2 for num in range(1, 21))
    print(squares_tuple)

generate_squares_tuple()


"""
Alternative Solution-3
"""

def generate_squares_tuple():
    print(tuple(num ** 2 for num in range(1, 21)))

generate_squares_tuple()

