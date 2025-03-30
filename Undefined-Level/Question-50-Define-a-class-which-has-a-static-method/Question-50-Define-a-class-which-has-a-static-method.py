"""
Question 50

Define a class named American which has a static method called printNationality.

Hints: Use @staticmethod decorator to define class static method.

Solution:
"""

class American:
    @staticmethod
    def print_nationality():
        print("American")

American.print_nationality()

"""
Alternative Solution-1
"""

class American:
    def print_nationality():
        print("American")
    
    print_nationality = staticmethod(print_nationality)

American.print_nationality()


"""
Alternative Solution-2
"""

def  print_nationality():
    print("American")

class American:
    print_nationality = staticmethod(print_nationality)

American.print_nationality()
