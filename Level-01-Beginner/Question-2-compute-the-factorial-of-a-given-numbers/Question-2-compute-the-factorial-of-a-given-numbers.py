"""
Level 1

Question-2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

"""

def myfact(x):
    if x == 0:
        return 1
    return x * myfact(x - 1)

x = int(input("Please enter an integer: "))
print(myfact(x))