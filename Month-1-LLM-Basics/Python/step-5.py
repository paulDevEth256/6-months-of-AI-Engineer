"""
step-5.py
Step 5: Functions and Scope
"""
# Basic function
def add(a, b=0):
    return a + b

# *args, **kwargs
def demo(*args, **kwargs):
    print(args, kwargs)

# Lambda and closure
square = lambda x: x*x
def make_adder(n):
    return lambda x: x + n

adder5 = make_adder(5)
print(add(3,4), square(5), adder5(10))

# Scope: local, global, nonlocal
x = 1
def outer():
    x = 2
    def inner():
        nonlocal x
        x = 3
    inner()
    return x
print(outer())
