Question 42

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values 
in one line and the last half values in one line.

Hints:

Use [n1:n2] notation to get a slice from a tuple.

Consider the PEP 8 - Style Guide. Naming a class: PrintValue . Naming a method: print_value .

https://peps.python.org/pep-0008/

Solution:

```python
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)
```
