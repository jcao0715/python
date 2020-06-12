# if statements
x = int(input("Please enter an int: "))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

# for loops
words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))

# range function - generates arithmetic progressions, it is not a list
for i in range(5):
	print(i)

for i in range(5, 10):
	print(i)

for i in range(0, 10, 3):
	print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])

print(sum(range(10)))

# break and continue statements
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		print(n, 'is a prime number')

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)

# pass - does nothing
# used when statement is requred syntactically but requires no action

# defining functions
# basically a method in java
def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()

f = fib #renamed function fib to f

def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

f100 = fib2(100)
print(f100)