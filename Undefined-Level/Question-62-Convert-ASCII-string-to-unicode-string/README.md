Question 62

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.

Solution:

In Python 3, the unicode() function has been removed.

```python
s = input()
print(s)
```

Alternative Solution:
```python
def ascii_to_utf8(ascii_string):
    ascii_bytes = ascii_string.encode('ascii')
    unicode_string = ascii_bytes.decode('utf-8')

    return unicode_string
```

Example usage

```python
ascii_string = "Hello, World!"
unicode_string = ascii_to_utf8(ascii_string)
print(unicode_string)
```
