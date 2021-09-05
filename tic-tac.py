

#find starting player 
def firstplayer():
    import random
    n = random.randint(1,2)
    firstplay = ""
    if n == 1:
        print("Player 1 you will go first")
        firstplay = "X"
    else:
        print("Player 2 you will go first")
        firstplay ="O"
    return firstplay

#building the grid
def buildgrid():
    grid = [[] for x in range(0,3)]
    for index in range(0,3):
        grid[index] = ["-" for y in range(0,3)]
#display the grid
    for r in grid:
        for c in r:
            print(c,end = " ")
        print()
    return grid

#get input
def getinput(grid):
    play_x = input("Enter a number between 0-2 for x:")
    if int(play_x) > 2:
        play_x = input("incorrect enter number between 0-2 only")
    play_y = input("Enter a number between 0-2 for y:")
    if int(play_y) > 2:
        play_y = input("incorrect enter number between 0-2 only")

    if grid[int(play_x)][int(play_y)] != "-":
        print("already taken try again!")
    return play_x,play_y


    
def checkwin(play_x,play_y,grid,counter):
    #check horizontal wins
    
    if grid[int(play_x)][0] == grid[int(play_x)][1] == grid[int(play_x)][2]:
        print(counter + " wins the game!")
        return True
        #check vertical
    elif grid[0][int(play_y)] == grid[1][int(play_y)] == grid[2][int(play_y)]:
        
        print(counter + " wins the game!")
        return True
        #check diagnol
    elif grid[0][0] == counter == grid[1][1] == grid[2][2] or grid[0][2] == counter == grid[1][1] == grid[2][0]:
        
        print(counter + " wins the game!")
        return True


def changecounter(counter):
    if counter == "X":
        counter = "O"
    else:
        counter = "X"
    return counter



def playgame():
    print("Hello welcome to tic tac toe, player 1 you will use X and player 2 you will use O")
    firstplay = firstplayer()
    grid = buildgrid()

    i = 0
    winner = False
    counter = firstplay

    while i < 9 and winner == False:
        x,y = getinput(grid)
        grid[int(x)][int(y)] = counter
        if checkwin(x,y,grid,counter) == True:
            winner = True
        else:
            counter = changecounter(counter)
            i += 1
        for r in grid:
            for c in r:
                print(c,end = " ")
            print()
    if i == 9:
        print("No winner game over!")
    else:
        print("game over!")

    playagain = input("Would you like to play again? Y/N:")
    if playagain == "Y":
        playgame()
    else:
        print("Goodbye!")



playgame()


