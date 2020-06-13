'''players = [1, 0]

choice = 1
for i in range(10):
	current_player = choice + 1
	print(current_player)
	choice = players[choice]'''

import itertools

player_choice = itertools.cycle([1, 2])

for i in range(10):
	print(next(player_choice))

#iterable: a thing we can iterate over
#iterator: a special object with next() method

x = [1, 2, 3, 4] #iterable

n = itertools.cycle(x) #iterator and iterable
print(next(n))

'''for i in n:
	print(i)'''

y = iter(x) #iterator and iterable

next(y)

#some iterators can be iterable
#strings and lists are iterable, but not iterators

game_size = 3

s = " "
for i in range(game_size):
	s += str(i) + "  "
s = "   " + "  ".join([str(i) for i in range(game_size)])

print(s)

dictionaries = {"key1" : 15, "key2" : 32}
print(dictionaries["key1"])
dictionaries["hithere"] = 92
print(dictionaries)