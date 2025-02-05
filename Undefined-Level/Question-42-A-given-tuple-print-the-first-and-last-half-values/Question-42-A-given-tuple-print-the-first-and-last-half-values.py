"""
Question 42

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values 
in one line and the last half values in one line.

Hints:

Use [n1:n2] notation to get a slice from a tuple.

Solution:
"""

tp = (1,2,3,4,5,6,7,8,9,10)
tp1 = tp[:5]
tp2 = tp[5:]
print(tp1)
print(tp2)
 
"""
Alternative Solution-1
"""
data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mid = len(data) // 2
print("First half:", data[:mid])
print("Second half:", data[mid:])


"""
Alternative Solution-2
"""
data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mid = len(data) // 2
print("First half:", *data[:mid])
print("Second half:", *data[mid:])



"""
Alternative Solution-3
"""

data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mid = len(data) // 2
print(*data[:mid])
print(*data[mid:])

