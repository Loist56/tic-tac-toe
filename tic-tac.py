print("Hello welcome to tic tac toe, player 1 you will use X and player 2 you will use O")

#find starting player 

import random
n = random.randint(1,2)
firstplay = ""
secondplay =""
if n == 1:
    print("Player 1 you will go first")
    firstplay = "X"
    secondplay = "O"
else:
    print("Player 2 you will go first")
    firstplay ="O"
    secondplay ="X"

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

#rest of the rounds

i = 1
winner = False
counter = secondplay
while i < 9 or winner == False:
    print(i)
    play_x = input("Enter a number between 0-2 for x:")
    if int(play_x) > 2:
        play_x = input("incorrect enter number between 0-2 only")
    play_y = input("Enter a number between 0-2 for y:")
    if int(play_y) > 2:
        play_y = input("incorrect enter number between 0-2 only")

    if grid[int(play_x)][int(play_y)] != 1:
        print("already taken try again!")
    else:
        grid[int(play_x)][int(play_y)] = counter
        if counter == secondplay:
            counter = firstplay
        else:
            counter = secondplay
        i = i+1
    for r in grid:
        for c in r:
            print(c,end = " ")
        print()
print("game over!")
        #need to check if they have won!!