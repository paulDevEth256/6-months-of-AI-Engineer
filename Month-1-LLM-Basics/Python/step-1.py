"""
step-1.py
Step 1: Variables and Data Types
"""
# Immutable vs mutable
a = 10               # int
b = 3.14             # float
c = True             # bool
d = "AI"             # str
e = None             # NoneType

lst = [1,2,3]        # list (mutable)
tpl = (1,2,3)        # tuple (immutable)
st = {1,2,3}         # set
dct = {"a":1, "b":2} # dict

print(type(a), type(lst), type(tpl), type(st), type(dct))
# Introspection
print(dir(lst))
