stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
stack.pop()

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()

squares = []
for x in range(10):
	squares.append(x ** 2)

# same as:
# squares = list(map(lambda x: x ** 2, range(10)))
# or
# squares = [x ** 2 for x in range(10)]

# combinations of sets
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# matrices
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8], 
	[9, 10, 11, 12],
	]
[[row[i] for row in matrix] for i in range(4)] # transposes matrix
list(zip(*matrix)) # alternative

a = [1, 2, 3, 4, 5, 6, 7, 8]
del a[0] # del deletes items from arrays
del a[2 : 4]
del a[:]

# tuples - immutable, can be nested
t = 123, 456, 'hello'
print(t[0])

empty = ()
single = 1,

# sets - unordered, no duplicates
a = set('abracadabra')
b = set('wobuffet')

# dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel['jack']
'guido' in tel

#looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'. format(q, a))

for i in reversed(range(1, 10, 2)):
	print(i)
	