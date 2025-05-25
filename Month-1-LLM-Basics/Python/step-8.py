"""
step-8.py
Step 8: Data Structures: Dictionaries
"""
d = {'a':1, 'b':2}
print(d.get('c', 0))
d['c'] = 3
print(d.keys(), d.values(), d.items())
# Methods
print(d.pop('b'), d.setdefault('d', 4))
print(d.update({'e':5}), d)
# Dict comprehension
dc = {x: x*x for x in range(3)}
print(dc)
