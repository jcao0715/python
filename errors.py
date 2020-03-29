while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("That was not a valid number. Please try again.")

# one try statement may have more than one except clause
# has optional "else" clause in case try clause does not raise an exception

# raise - forces a specified exeption to occur
# raise NameError('Hi there')

try:
	raise NameError('Hi')
except NameError:
	print('An exception flew by!')
	raise

try:
	raise KeyboardInterrupt
finally: # executes as last task before try statement completes
	print('Goodbye, world!')
