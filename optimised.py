grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_line(i):
    print ("|" + grid[i] + "|" + grid[i+1] + "|" + grid[i+2] + "|")

def print_grid():
    print ("-" * 7)
    print_line(0)
    print ("-" * 7)
    print_line(3)
    print ("-" * 7)
    print_line(6)
    print ("-" * 7)

def line_same(space1, space2, space3):
    return grid[space1] == grid[space2] == grid[space3]

def game_won():
    if line_same(0,1,2) or line_same(3,4,5) or line_same(6,7,8) \
        or line_same(0,3,6) or line_same(1,4,7) or line_same(2,5,8) \
        or line_same(0,4,8) or line_same(2,4,6):                   
        return True        

players = [''] * 2
players[0] = input ("Name of player 1 [X]:")
players[1] = input ("Name of player 2 [O]:")

markers = ["X", "O"]

turn = 0
print_grid()

while (turn < 9 and not game_won()):
    player = turn % 2 # Returns 0 if even, 1 if odd

    space = int(input(players[player] + " - Please choose a space:"))
    grid[space - 1] = markers[player]

    print_grid()
    turn+=1

if game_won():
    print(players[player] + " won!")
else:
    print("It's a draw!")