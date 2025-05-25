"""
step-15.py
Step 15: Advanced Topics (Decorators, Context Managers)
"""
from functools import wraps

# Decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

@timer
def compute(n):
    return sum(i*i for i in range(n))

compute(100000)

# Context manager via class
class Resource:
    def __enter__(self):
        print("Acquire")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Release")

with Resource():
    print("Using resource")

# Context manager via decorator
from contextlib import contextmanager

@contextmanager
def managed():
    print("Start")
    yield
    print("End")

with managed():
    print("Inside")
