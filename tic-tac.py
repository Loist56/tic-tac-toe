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

i = 0
winner = False
counter = firstplay
while i < 9 and winner == False:
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

        #check for winning

        #check horizontal wins
        if grid[int(play_x)][0] == grid[int(play_x)][1] == grid[int(play_x)][2]:
            winner = True
            print(counter + " wins the game!")
        #check vertical
        elif grid[0][int(play_y)] == grid[1][int(play_y)] == grid[2][int(play_y)]:
            winner = True
            print(counter + " wins the game!")
        #check diagnol
        elif grid[0][0] == counter == grid[1][1] == grid[2][2] or grid[0][2] == counter == grid[1][1] == grid[2][0]:
            winner = True
            print(counter + " wins the game!")
        else:
            if counter == firstplay:
                counter = secondplay
            else:
                counter = firstplay
                i = i+1

        



    for r in grid:
        for c in r:
            print(c,end = " ")
        print()
print("game over!")
        