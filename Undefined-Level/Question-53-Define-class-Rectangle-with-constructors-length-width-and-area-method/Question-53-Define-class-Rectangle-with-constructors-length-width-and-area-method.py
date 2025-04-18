"""
Question 53:

Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.

Hints:

Use def method_name to define a method.

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:

"""

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def area(self):
        return self.length * self.width

"""
Example usage
"""

a_rectangle = Rectangle(2,10)
print(a_rectangle.area())



"""
Alternative Solution:
"""

class Rectangle:
    def __init__(self, l: float, w: float):
        if l <= 0 or w <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self._length = l
        self._width = w
    
    @property
    def length(self) -> float:
        return self._length
    
    @length.setter
    def length(self, value: float):
        if value <= 0:
            raise ValueError("Length must be a positive number.")
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float):
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self._width = value
    
    def area(self) -> float:
        return self._length * self._width



"""
Example usage
"""

a_rectangle = Rectangle(2,10)
print(a_rectangle.area())
