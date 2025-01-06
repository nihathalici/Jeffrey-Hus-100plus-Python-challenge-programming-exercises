Question 38


Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list. Use [n1:n2] to slice a list

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:

```python
def generate_squares():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(li[:5])

generate_squares()
```

1. Alternative Solution

```python
def generate_squares():
    squares = []
    for i in range(1, 21):
        square = i ** 2
        squares.append(square)
    print(square[:5])

generate_squares()
```

2. Alternative Solution

```python
def generate_squares():
    squares = [i ** 2 for i in range(1, 21)]
    print(squares[:5])

generate_squares()
```
