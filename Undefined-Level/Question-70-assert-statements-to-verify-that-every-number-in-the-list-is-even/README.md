Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints: Use "assert expression" to make assertion.

Solution:

```python
li = [2, 4, 6, 8]
for i in li:
    assert i%2==0
```

Alternative Solutions:

```python
li = [2, 4, 6, 8]

# Alternative 1: Using all() with a generator expression
assert all(num % 2 == 0 for num in li), "Not all numbers are even"

# Alternative 2: Using list comprehension with assert on the whole list
assert [num % 2 == 0 for num in li] == [True, True, True, True], "Not all numbers are even"

# Alternative 3: Asserting the list length after filtering
assert len([num for num in li if num % 2 == 0]) == len(li), "Not all numbers are even"

# Alternative 4: Using map() function
assert all(map(lambda x: x % 2 == 0, li)), "Not all numbers are even"
```
