Question 56

Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.

Solution:

```python
def throws():
    return 5 / 0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception as err:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
```

Alternative Solution:

```python
def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError as e:
        result = str(e)
    return result

divide_by_zero()
```
