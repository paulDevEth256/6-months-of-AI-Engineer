"""
step-4.py
Step 4: Loops (for, while)
"""
# for loop
for i in range(5):
    print(i, end=" ")
print()

# iterate list with enumerate and zip
letters = ['a','b','c']
nums = [1,2,3]
for idx, val in enumerate(letters):
    print(idx, val)
for l,n in zip(letters, nums):
    print(l, n)

# while loop
count = 3
while count > 0:
    print(count)
    count -= 1
# break/continue
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
