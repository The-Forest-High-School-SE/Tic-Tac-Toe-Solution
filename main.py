grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_grid():
    print ("-" * 7)
    print ("|" + grid[0] + "|" + grid[1] + "|" + grid[2] + "|")
    print ("-" * 7)
    print ("|" + grid[3] + "|" + grid[4] + "|" + grid[5] + "|")
    print ("-" * 7)
    print ("|" + grid[6] + "|" + grid[7] + "|" + grid[8] + "|")
    print ("-" * 7)

print_grid()

player_1 = input ("Name of player 1 [X]:")
player_2 = input ("Name of player 2 [O]:")

def game_won():
    if line_same(0,1,2) or line_same(3,4,5) or line_same(6,7,8) \
        or line_same(0,3,6) or line_same(1,4,7) or line_same(2,5,8) \
        or line_same(0,4,8) or line_same(2,4,6):                   
        return True
        
def line_same(space1, space2, space3):
    return grid[space1] == grid[space2] == grid[space3]

turn = 0
while (turn < 9 and not game_won()):
    turn+=1
    if turn % 2:
        space = int(input("Player 1's turn - please choose a space " + player_1 + ":"))
        grid[space - 1] = "X"
    else:
        space = int(input("Player 2's turn - please choose a space " + player_2 + ":"))
        grid[space - 1] = "O"
    print_grid()

if game_won():
    if turn % 2:
        print("Player 1 won!")
    else:
        print("Player 2 won!")
else:
    print("It's a draw!")