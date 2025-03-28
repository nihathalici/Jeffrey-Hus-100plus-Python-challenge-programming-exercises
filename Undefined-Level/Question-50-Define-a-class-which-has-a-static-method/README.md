Question 50

Define a class named American which has a static method called printNationality.

Hints: Use @staticmethod decorator to define class static method.

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value . https://peps.python.org/pep-0008/

Solution:

```python
class American:
    @staticmethod
    def print_nationality():
        print("American")

American.print_nationality()
```

Alternative Solution-1

```python
class American:
    def print_nationality():
        print("American")
    
    print_nationality = staticmethod(print_nationality)

American.print_nationality()
```

Alternative Solution-2

```python
def  print_nationality():
    print("American")

class American:
    print_nationality = staticmethod(print_nationality)

American.print_nationality()
```
