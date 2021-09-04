print("Hello welcome to tic tac toe, player 1 you will use X and player 2 you will use O")

#find starting player 

import random
n = random.randint(1,2)
if n == 1:
    print("Player 1 you will go first")
else:
    print("Player 2 you will go first")

#building the grid
grid = [[] for x in range(0,3)]
for index in range(0,3):
    grid[index] = [1 for y in range(0,3)]
#display the grid
for r in grid:
    for c in r:
        print(c,end = " ")
    print()

