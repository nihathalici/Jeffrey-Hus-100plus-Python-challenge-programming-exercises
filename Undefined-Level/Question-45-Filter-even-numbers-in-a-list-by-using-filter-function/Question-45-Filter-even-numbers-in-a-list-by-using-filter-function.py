"""
Question 45

Write a program which can filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list. Use lambda to define anonymous functions.

Solution:
"""

li = [1,2,3,4,5,6,7,8,9,10]
even_numbers = filter(lambda x: x % 2 == 0, li)
print(*even_numbers, sep=", ")


"""
Alternative Solution-1
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


"""
Alternative Solution-2
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, numbers)))
