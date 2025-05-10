Question 57

Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.

Solution:

```python
class MyError(Exception):
    """ My own exception class
    
    Attributes:
        msg -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg
```

Example usage:

```python
custom_err = MyError("This is a self defined Custom Exception")

try:
    raise custom_err
except MyError as e:
    print(f"Caught an exception: {e.msg}")
```

Alternative Solution:

```python
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
```

Example usage:

```python
try:
    raise CustomException("This is a custom exception message.")
except CustomException as e:
    print(f"Caught an exception: {e.message}")
```
