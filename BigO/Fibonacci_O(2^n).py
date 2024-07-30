# Fibonacci 

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(30))
# nesse exemplo chamamos uma O (2^n)