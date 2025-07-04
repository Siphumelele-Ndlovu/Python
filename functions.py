# Functions in Python
"""
def greet(name):
    print(f"Hello, {name}")

greet("Siphumelele")

def add(a, b):
    return a + b
result = add(5, 3)
print(result)
"""


# Functions in Python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}!")

    greet("Alice")