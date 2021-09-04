print("Hello welcome to tic tac toe, player 1 you will use X and player 2 you will use O")

#find starting player 

import random
n = random.randint(1,2)
firstplay = ""
if n == 1:
    print("Player 1 you will go first")
    firstplay = "X"
else:
    print("Player 2 you will go first")
    firstplay ="O"

#building the grid
grid = [[] for x in range(0,3)]
for index in range(0,3):
    grid[index] = [1 for y in range(0,3)]
#display the grid
for r in grid:
    for c in r:
        print(c,end = " ")
    print()

#play game

#round1
firstplay_x = input("First player enter a number between 0-2 for x coordinate:")
if int(firstplay_x) > 2:
    firstplay_x = input("incorrect please enter a number between 0-2:")
firstplay_y = input("First player enter a number between 0-2 for y coordinate:")
if int(firstplay_y) > 2:
    firstplay_y = input("incorrect please enter a number between 0-2:")

grid[int(firstplay_x)][int(firstplay_y)] = firstplay 
for r in grid:
    for c in r:
        print(c,end = " ")
    print()

