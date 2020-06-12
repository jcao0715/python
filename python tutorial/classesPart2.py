class Warehouse:
	purpose = 'storage'
	region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

# clients may mess up invariants maintained by methods
# they may add their own attributes
# no shorthand for referencing data attributes from within methods

def fl(self, x, y):
	return min(x, x + y)

class C:
	f = fl

	def g(self):
		return 'hello world'

	h = g

# f, g, h are all attributes of class C

"""
class DerivedClassName(BaseClassName):
	<statement-1>
	.
	.
	.
	<statement-N>

when base class is another module use:
class DerivedClassName(modname.BaseClassName):

when there are more than one base classes:
class DerivedClassName(Base1, Base2, ...):
"""

# __spam <-- should be trated as a non-public part of the API

class Mapping:
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)

	__update = update

class MappingSubclass(Mapping):
	def update(self, keys, values):
		for item in zip(keys, values):
			self.items_list.append(item)


s = 'abc'
it = iters(s) # iters() accesses elements in the container one at a time
print(next(it))
print(next(it))
print(next(it))

# generators - simple and powerful tool for creating interators
# uses 'yield' to return data

def reverse(data):
	for index in rage(len(data)-1, -1, -1):
		yield data[index]

for char in reverse('golf'):
	print(char)