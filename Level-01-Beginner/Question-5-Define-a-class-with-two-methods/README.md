Question 5

Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

Solution:

```python

class InOutStr():
    def __init__(self):
        self.s = ""
    
    def getStr(self):
        self.s = input("Write something: ")

    def printStr(self):
        print(self.s.upper())

newstrObj = InOutStr()
newstrObj.getStr()
newstrObj.printStr()
```
