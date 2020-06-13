game_size = 3

'''game = []

for i in range(game_size):
	row = []
	for i in range(game_size):
		row.append(0)
	game.append(row)'''
game_size = input("What size game for tic tac toe?")
game = [[0 for i in range(game_size)] for i in range(game_size)]


print(game)