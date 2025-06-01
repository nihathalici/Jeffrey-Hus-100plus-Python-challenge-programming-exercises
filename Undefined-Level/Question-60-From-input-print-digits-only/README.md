Question 60

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example: If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use re.findall() to find all substring using regex.

```python
import re

inp_str = input("Enter a sequence of words separated by whitespace.")
print(re.findall("\d+", inp_str))
```

Alternative Solution-1:

```python
def extract_digit_words(inp_str):

    if not isinstance(inp_str, str):
        raise ValueError("Input must be a string.")

    words = inp_str.split()
    digit_words = [word for word in words if word.isdigit()]

    return digit_words
```

```python
def main():
    while True:
        try:
            inp_str = input("Enter a sequence of words separated by whitespace (or 'exit' to quit): ")
            if inp_str.lower() == 'exit':
                break
            result = extract_digit_words(inp_str)
            print(result)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
