Question 58

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.

Solution:

```python
import re

email_address = input("Enter an email address: ")
pattern = "(\w+)@((\w+\.)+(com))"
match = re.match(pattern, email_address) 
print(match.group(1))
```

Alternative Solution-1:


```python
import re

def extract_username(email):
    pattern = r"([a-zA-Z]+)@[a-zA-Z]+\.[a-zA-Z]+"
    match = re.match(pattern, email)

    if match:
        return match.group(1)
    else:
        return "This email address is invalid."
```

Example usage:

```python
email_address = input("Enter an email address: ")
username = extract_username(email_address)
print(username)
```

Alternative Solution-2:

```python
def extract_username(email):
    username = email.split('@')[0]
    return username
```



