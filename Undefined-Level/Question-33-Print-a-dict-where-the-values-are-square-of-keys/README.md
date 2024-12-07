Question 33

Define a function which can print a dictionary where the keys are numbers between 1 and 3 
(both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:
```python
def print_sqrs():
    d = dict()
    d[1] = 1
    d[2] = 2 ** 2
    d[3] = 3 ** 2
    print(d)

print_sqrs()
```

Alternative Solution:

```python
def print_sqrs():
    """
    Returns a dictionary containing the squares of the numbers 1 to 3.
    """
    sqrs = {i: i**2 for i in range(1, 4)}
    print(sqrs)

print_sqrs()
```
