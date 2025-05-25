"""
step-13.py
Step 13: Object-Oriented Programming
"""
class Animal:
    kind = "generic"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    kind = "dog"
    def speak(self):
        super().speak()
        print(f"{self.name} barks")

a = Animal("X")
d = Dog("Rex")
a.speak(); d.speak()
# Class/static methods and properties
class C:
    @staticmethod
    def sm(): print("static")
    @classmethod
    def cm(cls): print("class", cls)
    @property
    def prop(self): return "prop"
C.sm(); C.cm(); print(C().prop)
