year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# str() - returns representations of value which are human-readable
# repr() - genereates representations which can be read by interpreter
s = 'Hello, world'
print(str(s))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y)
print(s)

# open() returns a file object
# good practice to use "with" when dealing with file objects
# read(), readline() reads the file
# write("...") writes in the file