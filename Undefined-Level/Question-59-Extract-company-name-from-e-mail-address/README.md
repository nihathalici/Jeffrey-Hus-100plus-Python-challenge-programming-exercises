Question 59

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. 
Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.

Solution:

```python
import re

email_address = input("Enter an email address: ")
pattern = "(\w+)@(\w+)\.(com)"
match = re.match(pattern,email_address)
print(match.group(2))
```

Alternative Solution-1:

```python
import re

def extract_company_name(email):
    pattern = r"^[a-zA-Z]+@([a-zA-Z]+)\.com$"
    match = re.match(pattern, email)

    if match:
        return match.group(1)
    else:
        return "Invalid email format"
```

Example usage:

```python
email_inp = input("Enter an email address: ")
company_name = extract_company_name(email_inp)
print(company_name)
```

Alternative Solution-2:

```python
def extract_company_name(email):
    parts = email.split("@")

    if len(parts) != 2:
        return "Invalid email format"
    
    company_domain = parts[1].split(".")

    if len(company_domain) < 1:
        return "Invalid email format"
    
    company_name = company_domain[0]

    return company_name
```

Example usage:

```python
email_inp = input("Enter an email address: ")
company_name = extract_company_name(email_inp)
print(company_name)
```
