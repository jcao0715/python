def ask_ok(prompt, retries = 4, reminder = 'Please try again'):
	while True:
		ok = input(prompt)
		if ok in('y', 'ye', 'yes'): # in tests if a sequence contains a certain value
			return True
		if ok in('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)

def f(a, L = []):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))
# this function accumulates arguments

def f2(a, L = None):
	if L is None:
		L = []
	L.append(a)
	return L
# this function does not accumulate arguments

# functions can be called in many different ways
def parrot(voltage, state = 'a stiff', action = 'voom', types = 'blue'):
	print("This parrot wouldn't", action, end = ' ')
	print("if you put", voltage, "volts through it.")
	print("Lovely plumage, the", types)
	print("It's", state, "!")

parrot(1000)
parrot(voltage = 100)
parrot(voltage = 10, action = 'vroom')
parrot('ok', 'berefit of life', 'jump')
# must have at least one argument
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# * indicates a variable number for that argument
# * accumulates for each arg
def cheeseshop(kind, *arguments, **keywords):
	print("Do you have any", kind, "?")
	print("I'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("_" * 40)
	for kw in keywords:
		print(kw, ":", keywords[kw])

cheeseshop("Limburger",
			"It's runny sir.", "It's very runny, sir", 
			shopkeeper = 'Michael', client = 'John', sketch = 'cheeseshop sketch')

# restricted to use only positional parameters
def func1(arg, /):
	print(arg)

# restricted to use only keyword arguments
def func2(*, arg):
	print(arg)

# combines positional, standard, and keyword
def func3(pos_only, /, standard, *, kwd_only):
	print(pos_only, standard, kwd_only)

# pos-only when you don't want name of parameters to be available to user
# kwd-only when names have a meaning

# lambda returns the sum of its two arguments
# lambda a, b: a + b
def make_incrementor(n):
	return lambda x: x + n

make_incrementor(42)
make_incrementor(0)