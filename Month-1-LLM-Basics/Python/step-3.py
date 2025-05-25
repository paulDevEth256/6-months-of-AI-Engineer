"""
step-3.py
Step 3: Conditional Statements
"""
def sign(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
print(sign(10), sign(-5), sign(0))
# Ternary
age = 20
status = "adult" if age>=18 else "minor"
print(status)
