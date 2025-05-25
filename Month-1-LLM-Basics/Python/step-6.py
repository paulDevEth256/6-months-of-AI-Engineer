"""
step-6.py
Step 6: Data Structures: Lists
"""
nums = [5,2,9,1]
# Methods
nums.append(7)
nums.insert(1,8)
nums.extend([0,3])
print(nums)
print(nums.pop(), nums.remove(9))
print(sorted(nums), nums.reverse() or nums)
# Comprehensions
squares = [x*x for x in nums if x%2==0]
print(squares)
