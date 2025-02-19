"""
Question 44

Write a program which accepts a string as input to print "Yes" if the string is "yes" 
or "YES" or "Yes", otherwise print "No".

Hints:

Use if statement to judge condition.

Solution:
"""

s = input()
if s == "yes" or s == "YES" or s == "Yes":
    print("Yes")
else:
    print("No")


"""
Alternative Solution-1
"""

def check_yes(inp_str):
    if inp_str in ["yes", "YES", "Yes"]:
        print("Yes")
    else:
        print("No")

user_inp = input("Enter a string: ")
check_yes(user_inp)


"""
Alternative Solution-2
"""

user_inp = input("Enter a string: ")
print("Yes" if user_inp in ["yes", "YES", "Yes"] else "No")


"""
Alternative Solution-3
"""

print("Yes" if input("Enter a string: ").lower() == "yes" else "No")

