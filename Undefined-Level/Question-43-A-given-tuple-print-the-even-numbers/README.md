Question 43

Write a program to generate and print a tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

Hints:

Use "for" to iterate the tuple Use tuple() to generate a tuple from a list.

Solution:

```python
tp = (1,2,3,4,5,6,7,8,9,10)
li = list()
for num in tp:
	if num % 2 == 0:
		li.append(num)
tp2 = tuple(li)
print(tp2)
```

Alternative Solution-1
```python
original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_tuple = tuple(x for x in original_tuple if x % 2 == 0)
print(even_tuple)
```

Alternative Solution-2
```python
original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple(x for x in original_tuple if x % 2 == 0))
```

Alternative Solution-3
```python
print(tuple(x for x in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) if x % 2 == 0))
```
