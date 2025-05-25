"""
step-10.py
Step 10: File I/O
"""
# Text mode
with open('example.txt', 'w') as f:
    f.write("Line1\nLine2")
with open('example.txt', 'r') as f:
    print(f.read())
# Binary mode
with open('example.bin', 'wb') as f:
    f.write(b'\x00\x01')
with open('example.bin', 'rb') as f:
    print(f.read())
