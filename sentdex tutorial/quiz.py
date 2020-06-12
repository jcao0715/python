x = 1
def test():
    x = 2
test()
print(x) #1


x = 1
def test():
    global x
    x = 2
test()
print(x) #2


x = [1]
def test():
    x = [2]
test()
print(x) #2 X correct:1


x = [1]
def test():
    global x
    x = [2]
test()
print(x) #2


x = [1]
def test():
    x[0] = 2
test()
print(x) #1 X correct:2