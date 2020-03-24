# access interpreter using "python"
# _ is assigned the last printed expression
# integers are int
# decimals are floats
# complex numbers can be expessed with j (ex. 3 + 5j)
word = 'python'
print(word[2])
print(word[-1])
print(word[2 : 5])
print(word[ : 2])
print(word[2 : ])
print(len(word))
#strings are essentially a list of letters

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares + [36, 64])
squares[3] = 10
print(squares.append(36))
squares[ : ] = [ ] # clears the list
print(len(squares))

# while loop
a, b = 0, 1
while a < 10:
	print(a)
	a, b = b, a + b

a, b = 0, 1
while a < 1000:
	print(a) 
   #print(a, end = ', ') end avoids making a new line 
	a, b = b, a + b