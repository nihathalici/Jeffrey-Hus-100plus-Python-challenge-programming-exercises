Question 51

Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.

Solution:

```python
class American:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}, an American."

class NewYorker(American):
    def __init__(self, name, borough):
        super().__init__(name)
        self.borough = borough

    def greet(self):
        return f"Hello, I'm {self.name}, a New Yorker from {self.borough}."

    def favorite_spot(self):
        return f"My favorite spot in New York is Central Park."
```

Creating instances of the classes

```python
american = American(name="John")
print(american.greet())  # Prints: Hello, I'm John, an American.

new_yorker = NewYorker(name="James", borough="Harlem")
print(new_yorker.greet())  # Prints: Hello, I'm James, a New Yorker from Harlem.
print(new_yorker.favorite_spot())  # Prints: My favorite spot in New York is Central Park.
```
