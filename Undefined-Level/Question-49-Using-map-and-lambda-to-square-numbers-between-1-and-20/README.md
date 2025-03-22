Question 49

Write a program which can map() to make a list whose elements are square 
of numbers between 1 and 20 (both included).

Hints Use map() to generate a list. Use lambda to define anonymous functions.

Solution:

```python
sq_num = map(lambda x: x ** 2, range(1, 21))
print(*sq_num, sep = ", ")
```

Alternative Solution-1
```python
sq_num = list(map(lambda x: x ** 2, range(1, 21)))
print(sq_num)
```

Alternative Solution-2
```python
squares = [x**2 for x in range(1, 21)]
print(squares)
```
