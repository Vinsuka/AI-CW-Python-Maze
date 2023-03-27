import random

START = "S |"
GOAL = "G |"
BLOCK = "X |"
NAVIGATE = "* |"
count = 4  # the amount of Blocks
TotalTime = 0  # total time taken
BestPathTime = 0  # optimal time taken
previousPositions = []  # array to record previous positions
previousRows = []  # array to record previous rows

# Creating Maze in a 2D array
Maze = [
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
Maze[select_StartRow][select_StartingPosition] = START
Maze[select_GoalRow][select_GoalPosition] = GOAL

# since there need to be 4 blocks
while count > 0:
    randomRowBlock = random.randrange(1, 6)
    randomPositionBlock = random.randrange(1, 7)
    count = count - 1

    if Maze[randomRowBlock][randomPositionBlock] == "  |":
        Maze[randomRowBlock][randomPositionBlock] = BLOCK
    else:
        count = count + 1

# DFS maze Navigation
currentRow = select_StartRow
currentPosition = select_StartingPosition


# Print maze
def output():
    # output
    for r in Maze:
        for c in r:
            print(c, end=" ")
        print()


# looking around
previousRows.append(currentRow)
previousPositions.append(currentPosition)
while True:
    Check = 0
    TotalTime = TotalTime + 1
    BestPathTime = BestPathTime + 1

    # Checking West for available space
    if Maze[currentRow][currentPosition - 1] == "  |":
        currentPosition = currentPosition - 1
        Maze[currentRow][currentPosition] = NAVIGATE
        print("Can Move West")
    # Checking West for goal
    elif Maze[currentRow][currentPosition - 1] == GOAL:
        print("GOAL Achieved")
        break

    # Checking North West for available space
    elif Maze[currentRow-1][currentPosition-1] == "  |":
        currentRow = currentRow - 1
        currentPosition = currentPosition - 1
        Maze[currentRow][currentPosition] = NAVIGATE
        print("Can Move North West")
    elif Maze[currentRow-1][currentPosition-1] == GOAL:
        print("GOAL Achieved")
        break

    # Checking North for available space
    elif Maze[currentRow - 1][currentPosition] == "  |":
        currentRow = currentRow - 1
        Maze[currentRow][currentPosition] = NAVIGATE
        print("Can Move North")
    # Checking North for goal
    elif Maze[currentRow - 1][currentPosition] == GOAL:
        print("GOAL Achieved")
        break

    # Checking North East for available space
    elif Maze[currentRow-1][currentPosition+1] == "  |":
        currentRow = currentRow - 1
        currentPosition = currentPosition + 1
        Maze[currentRow][currentPosition] = NAVIGATE
        print("Can Move North East")
    elif Maze[currentRow-1][currentPosition+1] == GOAL:
        print("GOAL Achieved")
        break

    # checking East for available space
    elif Maze[currentRow][currentPosition + 1] == "  |":
        currentPosition = currentPosition + 1
        Maze[currentRow][currentPosition] = NAVIGATE
        print("Can Move East")
        # checking East for goal
    elif Maze[currentRow][currentPosition + 1] == GOAL:
        print("GOAL Achieved")
        break

    # Checking South East for available space
    elif Maze[currentRow+1][currentPosition+1] == "  |":
        currentRow = currentRow + 1
        currentPosition = currentPosition + 1
        Maze[currentRow][currentPosition] = NAVIGATE
        print("Can Move South East")
    elif Maze[currentRow+1][currentPosition+1] == GOAL:
        print("GOAL Achieved")
        break

    # Checking South for available space
    elif Maze[currentRow + 1][currentPosition] == "  |":
        currentRow = currentRow + 1
        Maze[currentRow][currentPosition] = NAVIGATE
        print("Can Move South")
    # checking South for goal
    elif Maze[currentRow + 1][currentPosition] == GOAL:
        print("GOAL Achieved")
        break

    # Checking South West for available space
    elif Maze[currentRow-1][currentPosition-1] == "  |":
        currentRow = currentRow - 1
        currentPosition = currentPosition - 1
        Maze[currentRow][currentPosition] = NAVIGATE
        print("Can Move South West")
    elif Maze[currentRow-1][currentPosition-1] == GOAL:
        print("GOAL Achieved")
        break

    output()

print("Total Time Taken : ", +TotalTime)
print("Best Time Taken : ", +BestPathTime)

