Question 36

Define a function which can generate a dictionary where the keys are numbers between 1 and 20
 (both included) and the values are square of keys. The function should just print the keys only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary. Use ** operator to get power of a number. Use range() for loops. Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:

```python
def print_squares():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for k in d.keys():
        print(k)
```

"""
1. Alternative Solution:
"""

def print_squares():
    d = {i: i ** 2 for i in range(1, 21)}
    for k in d.keys():
        print(k)
