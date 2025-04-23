Define a class named Shape and its subclass Square. The Square class has an init function 
which takes a length as argument. Both classes have a area function which can print 
the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.


Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:

```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l
    
    def area(self):
        return self.length * self.length
```

Example usage

```python
a_square= Square(3)
print(a_square.area())
```

Alternative Solution:

```python
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
```

Example usage

```python
shape = Shape()
print("Area of generic shape:", shape.area())

square = Square(4)
print("Area of square:", square.area())
```
