# namespace - mapping from names to objects
# attribute - name following a dot

def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	def do_global():
		global spam
		spam = "global spam"

	spam = "test spam"
	do_local()
	print("After local assignment:", spam)
	do_nonlocal()
	print("After nonlocal assignment:", spam)
	do_global()
	print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


class MyClass:
	i = 12345

	def f(self):
		return 'hello world'

x = MyClass() # creates a new instance of MyClass

""" 
creates objects with instances customized to a specific initial state
def __init__(self):
	self.data = []
"""

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

"""
x.f() <-- f() is a method
x.f <-- f is a method object
"""

class Dog:

	kind = 'canine'
  # tricks = [] <-- creates a shared list between objects

	def __init__(self, name):
		self.name = name
		self.tricks = []

	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.name)
print(d.kind)
print(d.add_trick('roll over'))
print(d.tricks)
print(e.name)
print(e.kind)
print(e.add_trick('play dead'))
print(e.tricks)