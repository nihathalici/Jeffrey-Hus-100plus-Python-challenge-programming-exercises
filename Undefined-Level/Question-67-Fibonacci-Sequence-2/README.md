Question 67

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

Hints: We can define recursive function in Python. Use list comprehension to generate a list from an existing list. Use string.join() to join a list of strings.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

```python
def fibo_fn(n):
    fibo_seq = [0, 1]
    [fibo_seq.append(fibo_seq[-1] + fibo_seq[-2]) for _ in range(2, n+1)]
    return fibo_seq[:n+1]
```

Example usage:

```python
n = int(input("Enter the value of n: "))
print(",".join(map(str, fibo_fn(n))))
```

Alternative Solution:

```python
def fibonacci(n):
    if n == 0:
        return [0]
    fib_sequence = [0, 1]
    [fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) for _ in range(2, n+1)]
    return fib_sequence[:n+1]

def main():
    while True:
        try:
            n = int(input("Enter the value of n: "))
            if n < 0:
                print("Please enter a non-negative integer.")
            else:
                print(",".join(map(str, fibonacci(n))))
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
```

