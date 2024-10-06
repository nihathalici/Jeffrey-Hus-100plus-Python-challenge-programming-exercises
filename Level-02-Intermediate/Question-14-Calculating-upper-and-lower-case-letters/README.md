Question 14

Level 2

Question: Write a program that accepts a sentence and calculate the number
 of upper case letters and lower case letters. Suppose the following input 
is supplied to the program: 
Hello world! 
Then, the output should be: 
UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should be 
assumed to be a console input.

Solution:

```python
s = input("Enter a sentence with upper and lower case letters: ")

d = {"UPPER CASE": 0, "LOWER CASE": 0}

for ch in s:
    if ch.isupper():
        d["UPPER CASE"] += 1
    elif ch.islower():
        d["LOWER CASE"] += 1
    else:
        pass

print("UPPER CASE:",d["UPPER CASE"],"\n""LOWER CASE:",d["LOWER CASE"])
```
