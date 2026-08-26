Question 71

Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example: If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints: Use eval() to evaluate an expression.

Solution:
```python
expression = raw_input()
print(eval(expression))
```

#Alternative Solutions

```python
import operator
import re

def safe_eval(expression):
    # Only allow numbers, operators, parentheses, and spaces
    if not re.match(r'^[\d+\-*/().\s]+$', expression):
        raise ValueError("Invalid characters in expression")
    
    # Define allowed operations
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv,
        '%': operator.mod,
        '**': operator.pow
    }
    
    # Parse and evaluate manually
    try:
        # This is still eval but with a restricted namespace
        allowed_names = {k: v for k, v in ops.items()}
        allowed_names['__builtins__'] = None
        return eval(expression, {"__builtins__": None}, allowed_names)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

try:
    expression = input("Enter expression: ")
    result = safe_eval(expression)
    print(result)
except Exception as e:
    print(f"Error: {e}")
```
