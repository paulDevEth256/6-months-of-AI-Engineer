"""
step-12.py
Step 12: Comprehensions and Lambdas
"""
# List comprehension
nums = [1,2,3,4]
evens = [x for x in nums if x%2==0]
# Set comprehension
sq = {x*x for x in nums}
# Dict comprehension
d = {x: x*x for x in nums}
# Lambdas, map, filter, reduce
add = lambda a,b: a+b
from functools import reduce
print(list(map(lambda x: x*2, nums)))
print(list(filter(lambda x: x>2, nums)))
print(reduce(add, nums))
