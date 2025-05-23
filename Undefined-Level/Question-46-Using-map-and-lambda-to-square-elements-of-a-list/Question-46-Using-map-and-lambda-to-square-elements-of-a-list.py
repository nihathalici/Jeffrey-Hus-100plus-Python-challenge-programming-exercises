"""
Question 46

Write a program which can map() to make a list whose elements are square of elements 
in [1,2,3,4,5,6,7,8,9,10].

Hints Use map() to generate a list. Use lambda to define anonymous functions.

Solution:
"""

li = [1,2,3,4,5,6,7,8,9,10]
sq_num = map(lambda x: x ** 2, li)
print(*sq_num, sep = ", ")

"""
Alternative Solution-1
"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq_num = list(map(lambda x: x ** 2, num))
print(sq_num)



"""
Alternative Solution-2
"""

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
