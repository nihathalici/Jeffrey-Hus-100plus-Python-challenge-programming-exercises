"""
Question 48

Write a program which can filter() to make a list whose elements are even number 
between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list. Use lambda to define anonymous functions.

Solution:
"""

even_numbers = filter(lambda x: x % 2 == 0, range(1, 21))

print(*even_numbers, sep = ", ")

"""
Alternative Solution-1
"""
num = range(1, 21)
even_num = list(filter(lambda x: x % 2 == 0, num))
print(even_num)


"""
Alternative Solution-2
"""
even_num = list(filter(lambda x: x % 2 == 0, range(1, 21)))
print(even_num)
