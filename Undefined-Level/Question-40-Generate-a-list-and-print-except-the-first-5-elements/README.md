Question 40

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.

Hints:

Use ** operator to get power of a number. Use range() for loops. Use list.append() to add values into a list. Use [n1:n2] to slice a list

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:

```python
def generate_and_print_squares():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(li[5:])

generate_and_print_squares()
```

Alternative Solution-1:

```python
def generate_and_print_squares():
    sq_li = []
    for i in range(1, 21):
        sq_li.append(i ** 2)
    for val in sq_li[5:]:
        print(val)

generate_and_print_squares()
```
