import random

# define Variable
START = "S |"
GOAL = "G |"
BLOCK = "X |"
NAVIGATE = "* |"
Empty_Value = "  |"
count = 4  # the amount of Blocks
TotalTime = 0  # total time taken
BestPathTime = 0  # optimal time taken
previousPositions = []  # array to record previous positions
previousRows = []  # array to record previous rows

# Creating Maze in a 2D array
Maze1 = [
    [" ", " 0", "  1", "  2", "  3", "  4", "  5","",""],
    ["0|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["1|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["2|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["3|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["4|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["5|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["", "", "", "", "", "", "","",""]
]

Maze2 = [
    [" ", " 0", "  1", "  2", "  3", "  4", "  5","",""],
    ["0|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["1|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["2|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["3|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["4|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["5|", "  |", "  |", "  |", "  |", "  |", "  |", ""],
    ["", "", "", "", "", "", "","",""]
]
# since the starting poit of the maze has to be in between 0-11 we have to select either the first row or second row
# random Start Position

# random row selection
select_StartRow = random.randrange(1, 6)
# randomly get start position
select_StartingPosition = random.randrange(1, 3)

# randomly get goal position
select_GoalRow = random.randrange(1, 6)  # random row selection
# randomly get goal position
select_GoalPosition = random.randrange(5, 7)

# Creating the START and GOAL on the maze
Maze1[select_StartRow][select_StartingPosition] = START
Maze1[select_GoalRow][select_GoalPosition] = GOAL

Maze2[select_StartRow][select_StartingPosition] = START
Maze2[select_GoalRow][select_GoalPosition] = GOAL

# since there need to be 4 blocks
while count > 0:
    randomRowBlock = random.randrange(1, 6)
    randomPositionBlock = random.randrange(1, 7)
    count = count - 1

    if Maze1[randomRowBlock][randomPositionBlock] == "  |" and Maze2[randomRowBlock][randomPositionBlock] == "  |":
        Maze1[randomRowBlock][randomPositionBlock] = BLOCK
        Maze2[randomRowBlock][randomPositionBlock] = BLOCK
    else:
        count = count + 1

# DFS maze Navigation
currentRow = select_StartRow
currentPosition = select_StartingPosition
print("DFS MAZE")

# Print maze
def output():
    # output
    for r in Maze1:
        for c in r:
            print(c, end=" ")
        print()

output()
# looking around
previousRows.append(currentRow)
previousPositions.append(currentPosition)
while True:
    Check = 0
    TotalTime = TotalTime + 1
    BestPathTime = BestPathTime + 1

    # Checking West for available space
    if Maze1[currentRow][currentPosition - 1] == "  |":
        currentPosition = currentPosition - 1
        Maze1[currentRow][currentPosition] = NAVIGATE
        print("Can Move West")
    # Checking West for goal
    elif Maze1[currentRow][currentPosition - 1] == GOAL:
        print("GOAL Achieved")
        break

    # Checking North West for available space
    elif Maze1[currentRow-1][currentPosition-1] == "  |":
        currentRow = currentRow - 1
        currentPosition = currentPosition - 1
        Maze1[currentRow][currentPosition] = NAVIGATE
        print("Can Move North West")
    elif Maze1[currentRow-1][currentPosition-1] == GOAL:
        print("GOAL Achieved")
        break

    # Checking North for available space
    elif Maze1[currentRow - 1][currentPosition] == "  |":
        currentRow = currentRow - 1
        Maze1[currentRow][currentPosition] = NAVIGATE
        print("Can Move North")
    # Checking North for goal
    elif Maze1[currentRow - 1][currentPosition] == GOAL:
        print("GOAL Achieved")
        break

    # Checking North East for available space
    elif Maze1[currentRow-1][currentPosition+1] == "  |":
        currentRow = currentRow - 1
        currentPosition = currentPosition + 1
        Maze1[currentRow][currentPosition] = NAVIGATE
        print("Can Move North East")
    elif Maze1[currentRow-1][currentPosition+1] == GOAL:
        print("GOAL Achieved")
        break

    # checking East for available space
    elif Maze1[currentRow][currentPosition + 1] == "  |":
        currentPosition = currentPosition + 1
        Maze1[currentRow][currentPosition] = NAVIGATE
        print("Can Move East")
        # checking East for goal
    elif Maze1[currentRow][currentPosition + 1] == GOAL:
        print("GOAL Achieved")
        break

    # Checking South East for available space
    elif Maze1[currentRow+1][currentPosition+1] == "  |":
        currentRow = currentRow + 1
        currentPosition = currentPosition + 1
        Maze1[currentRow][currentPosition] = NAVIGATE
        print("Can Move South East")
    elif Maze1[currentRow+1][currentPosition+1] == GOAL:
        print("GOAL Achieved")
        break

    # Checking South for available space
    elif Maze1[currentRow + 1][currentPosition] == "  |":
        currentRow = currentRow + 1
        Maze1[currentRow][currentPosition] = NAVIGATE
        print("Can Move South")
    # checking South for goal
    elif Maze1[currentRow + 1][currentPosition] == GOAL:
        print("GOAL Achieved")
        break

    # Checking South West for available space
    elif Maze1[currentRow-1][currentPosition-1] == "  |":
        currentRow = currentRow - 1
        currentPosition = currentPosition - 1
        Maze1[currentRow][currentPosition] = NAVIGATE
        print("Can Move South West")
    elif Maze1[currentRow-1][currentPosition-1] == GOAL:
        print("GOAL Achieved")
        break

    # wrong way
    elif Maze1[currentRow][currentPosition] == BLOCK or START:
        print("Went on the Wrong Path")
        print("Retrace Step")
        BestPathTime = BestPathTime - 2
        # checking if the previous position is on the West
        if previousPositions[-2] - previousPositions[-1] == 1:
            currentPosition = previousPositions[-2]
        # checking if the previous position is on the North West
        elif previousPositions[-2] - previousPositions[-1] == 1 and previousRows[-2] - previousRows[-1] == 1:
            currentRow = previousRows[-2]
            currentPosition = previousPositions[-2]

        # checking if the previous position is on the North
        elif previousRows[-2] - previousRows[-1] == 1:
            currentRow = previousRows[-2]

        # Checking if the previous position is on the North East
        elif previousRows[-2] - previousRows[-1] == 1 and previousPositions[-2] - previousPositions[-1] == 1:
            currentRow = previousRows[-2]
            currentPosition = previousPositions[-2]

        # checking if the previous position is on the East
        elif previousPositions[-2] - previousPositions[-1] == 1:
            currentPosition = previousPositions[-2]

        # Checking if the previous position is on the South East
        elif previousPositions[-2] - previousPositions[-1] == 1 and previousRows[-2] - previousRows[-1] == 1:
            currentRow = previousRows[-2]
            currentPosition = previousPositions[-2]

        # checking if the previous position is on the South
        elif previousRows[-2] - previousRows[-1] == 1:
            currentRow = previousRows[-2]

        # checking if the previous position is on the South West
        elif previousRows[-2] - previousRows[-1] == 1 and previousPositions[-2] - previousPositions[-1] == 1:
            currentRow = previousRows[-2]
            currentPosition = previousPositions[-2]

        # removing previous path
        del previousRows[-1]
        del previousPositions[-1]
        Check = Check + 1
    # add to list if not in wrong path
    if Check == 0:
        previousRows.append(currentRow)
        previousPositions.append(currentPosition)

    output()

print("Total Time Taken : ", +TotalTime)
print("Best Time Taken : ", +BestPathTime)
print("++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++")

print("A * MAZE")
import random
TotalTime1 = 1  # total time taken

# Print maze
def output2():
    # output
    for r in Maze2:
        for c in r:
            print(c, end=" ")
        print()


# Chebyshev Distance
GoalRow = select_GoalRow
GoalPosition = select_GoalPosition

currentNodeRow = select_StartRow
currentNodePosition = select_StartingPosition
# ChebyshevDistance = max((currentNodePosition - GoalPosition) * (-1), (currentNodeRow - GoalRow) * (-1))
output2()
while True:
    checkWest = max(((currentNodePosition - 1) - GoalPosition) * (-1), (currentNodeRow - GoalRow) * (-1))
    checkNorthWest = max(((currentNodePosition - 1) - GoalPosition) * (-1), ((currentNodeRow - 1) - GoalRow) * (-1))
    checkNorth = max((currentNodePosition - GoalPosition) * (-1), ((currentNodeRow - 1) - GoalRow) * (-1))
    checkNorthEast = max(((currentNodePosition + 1) - GoalPosition) * (-1), ((currentNodeRow - 1) - GoalRow) * (-1))
    checkEast = max(((currentNodePosition + 1) - GoalPosition) * (-1), (currentNodeRow - GoalRow) * (-1))
    checkSouthEast = max(((currentNodePosition + 1) - GoalPosition) * (-1), ((currentNodeRow + 1) - GoalRow) * (-1))
    checkSouth = max((currentNodePosition - GoalPosition) * (-1), ((currentNodeRow + 1) - GoalRow) * (-1))
    checkSouthWest = max(((currentNodePosition - 1) - GoalPosition) * (-1), ((currentNodeRow + 1) - GoalRow) * (-1))
    arr = [checkWest,checkNorthWest,checkNorth,checkNorthEast,checkEast,checkSouthEast,checkSouth,checkSouthWest]
    loopCount = 0

    is_west_run = False
    is_north_west_run = False
    is_north_run = False
    is_north_east_run = False
    is_east_run = False
    is_south_east_run = False
    is_south_run = False
    is_south_west_run = False
    while True:

        minValue = min(arr)
        # check west
        if minValue == checkWest and not is_west_run:
            is_west_run = True
            if Maze2[currentNodeRow][currentNodePosition - 1 ] == Empty_Value or Maze2[currentNodeRow][currentNodePosition - 1 ] == GOAL:
                currentNodePosition = currentNodePosition - 1
                currentNodeRow = currentNodeRow
                print("can go West")
                break
            elif Maze2[currentNodeRow][currentNodePosition - 1] != Empty_Value or Maze2[currentNodeRow][currentNodePosition - 1] != GOAL:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check North West
        elif minValue == checkNorthWest and not is_north_west_run:
            is_north_west_run = True
            if Maze2[currentNodeRow - 1][currentNodePosition - 1 ] == Empty_Value or Maze2[currentNodeRow - 1][currentNodePosition - 1 ] ==  GOAL:
                currentNodePosition = currentNodePosition - 1
                currentNodeRow = currentNodeRow - 1
                print("can go North West")
                break
            elif Maze2[currentNodeRow - 1][currentNodePosition - 1] != Empty_Value or Maze2[currentNodeRow - 1][currentNodePosition - 1] != GOAL:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check North
        elif minValue == checkNorth and not is_north_run:
            is_north_run = True
            if Maze2[currentNodeRow - 1][currentNodePosition ] == Empty_Value or Maze2[currentNodeRow - 1][currentNodePosition ] == GOAL:
                currentNodePosition = currentNodePosition
                currentNodeRow = currentNodeRow - 1
                print("can go North")
                break
            elif Maze2[currentNodeRow - 1][currentNodePosition] != Empty_Value or Maze2[currentNodeRow - 1][currentNodePosition] !=GOAL:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check North East
        elif minValue == checkNorthEast and not is_north_east_run:
            is_north_east_run = True
            if Maze2[currentNodeRow - 1][currentNodePosition + 1 ] == Empty_Value or Maze2[currentNodeRow - 1][currentNodePosition + 1 ] == GOAL:
                currentNodePosition = currentNodePosition + 1
                currentNodeRow = currentNodeRow - 1
                print("can go North East")
                break
            elif Maze2[currentNodeRow - 1][currentNodePosition + 1] != Empty_Value or Maze2[currentNodeRow - 1][currentNodePosition + 1] !=  GOAL:
                loopCount = loopCount + 1
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check East
        elif minValue == checkEast and not is_east_run:
            is_east_run = True
            if Maze2[currentNodeRow][currentNodePosition + 1 ] == Empty_Value or Maze2[currentNodeRow][currentNodePosition + 1 ] == GOAL:
                currentNodePosition = currentNodePosition + 1
                currentNodeRow = currentNodeRow
                print("can go East")
                break
            elif Maze2[currentNodeRow][currentNodePosition + 1] != Empty_Value or Maze2[currentNodeRow][currentNodePosition + 1] != GOAL:
                loopCount = loopCount + 1
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check south East
        elif minValue == checkSouthEast and not is_south_east_run:
            is_south_east_run = True
            if Maze2[currentNodeRow + 1][currentNodePosition + 1] == Empty_Value or Maze2[currentNodeRow + 1][currentNodePosition + 1] == GOAL:
                currentNodePosition = currentNodePosition + 1
                currentNodeRow = currentNodeRow + 1
                print("can go South East")
                break
            elif Maze2[currentNodeRow + 1][currentNodePosition + 1] != Empty_Value or Maze2[currentNodeRow + 1][currentNodePosition + 1] != GOAL:
                loopCount = loopCount + 1
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check south
        elif minValue == checkSouth and not is_south_run:
            is_south_run = True
            if Maze2[currentNodeRow + 1][currentNodePosition] == Empty_Value or Maze2[currentNodeRow + 1][currentNodePosition] == GOAL:
                currentNodePosition = currentNodePosition
                currentNodeRow = currentNodeRow + 1
                print("can go south")
                break
            elif Maze2[currentNodeRow + 1][currentNodePosition] != Empty_Value or Maze2[currentNodeRow + 1][currentNodePosition] != GOAL:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break
        # check south West
        elif minValue == checkSouthWest and not is_south_west_run:
            is_south_west_run = True
            if Maze2[currentNodeRow + 1][currentNodePosition - 1 ] == Empty_Value or Maze2[currentNodeRow + 1][currentNodePosition - 1 ] == GOAL:
                currentNodePosition = currentNodePosition - 1
                currentNodeRow = currentNodeRow + 1
                print("can go south west")
                break
            elif Maze2[currentNodeRow + 1][currentNodePosition - 1 ] != Empty_Value or Maze2[currentNodeRow + 1][currentNodePosition - 1 ] != GOAL:
                for i in range(len(arr)):
                    if arr[i] == minValue:
                        del arr[i]
                        break

    if Maze2[currentNodeRow][currentNodePosition] == Empty_Value:
        Maze2[currentNodeRow][currentNodePosition] = NAVIGATE
        TotalTime1 = TotalTime1 + 1

    elif Maze2[currentNodeRow][currentNodePosition] == GOAL:
        output2()
        print("GOAL")
        print("Total Time taken: ",TotalTime1 + 1)
        print("_________________________________")
        print("_________________________________")
        break
    output2()


print("DFS VS A STAR outcome")
print("---------------------------------")
print("DFS")
print("Total Time Taken : ", +TotalTime)
print("Best Time Taken : ", +BestPathTime)
print("---------------------------------")
print("A star")
print("Total Time Taken : ", +TotalTime1)
