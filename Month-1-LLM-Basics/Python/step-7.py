"""
step-7.py
Step 7: Data Structures: Tuples and Sets
"""
# Tuples
t = (1,2,3,2)
print(t.count(2), t.index(3))
# Sets
s = {1,2,3}
s.add(4)
s.remove(2)
print(s, 3 in s)
print(s.union({5}), s.intersection({3,4,5}), s.difference({1,4}))
# Set comprehension
sq = {x*x for x in range(5)}
print(sq)
