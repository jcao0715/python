'''l = [1, 2, 3, 4, 5]

print(l)

l[1] = 99

print(l)

def addition(x, y):
    return x+y

print(addition(5,3))

z = addition("hey"," there")

print(z)

game = "I want to play a game"
print(id(game))
#strings are immutable

def game_board(player=0, row=0, column=0, just_display=False):
    global game
    #global let's you permanently modify an object
    game = "A game"
    print(id(game))
    print(game)

game_board()
print(game)
print(id(game))'''


game = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:    
        print("     0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)

        return game_map
    
    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2", e)

    except Exception as e:
        print("Something went very wrong!", e)


game = game_board(game, just_display=True)
game = game_board(game_board, player=1, row=3, column=1)