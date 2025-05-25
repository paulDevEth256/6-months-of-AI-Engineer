"""
step-9.py
Step 9: String Manipulation
"""
s = "Hello, AI"
print(s.upper(), s.lower(), s.title(), s.strip(', AI'))
print(s.split(','), '-'.join(s.split()), s.replace('AI', 'Python'))
# Formatting
name = "Dev"
print("Hello {}".format(name), f"Hi {name}", "%s %s" % ("Hey", name))
