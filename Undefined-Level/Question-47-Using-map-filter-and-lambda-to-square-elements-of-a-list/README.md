Question 47

Write a program which can map() and filter() to make a list whose elements are square of 
even number in [1,2,3,4,5,6,7,8,9,10].

Hints Use map() to generate a list. Use filter() to filter elements of a list. Use lambda to define anonymous functions.

Solution:

```python
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq_even_num = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, num))
print(*sq_even_num, sep = ", ")
```

Alternative Solution-1

```python
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = filter(lambda x: x % 2 == 0, num)
sq_even_num = map(lambda x: x ** 2, even_num)
result = list(sq_even_num)
print(result)
```

Alternative Solution-2

```python
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, num)))
```
