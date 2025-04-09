Question 52

Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.

Solution:

```python
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
```

Example usage

```python
a_circle = Circle(2)
print(a_circle.area())
```

Alternative Solution:

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def compute_area(self):
        return math.pi * self.radius ** 2
```
