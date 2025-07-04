Question 66

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints: We can define recursive function in Python.

Solution:

```python
def fibo_fn(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_fn(n-1) + fibo_fn(n-2)
```

Example usage:

```python
print(fibo_fn(7))
```

Alternative Solution-1:

```python
def fibo_fn(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_fn(n-1) + fibo_fn(n-2)
```
