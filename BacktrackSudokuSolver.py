"""Solving a sudoku puzzle using backtracking"""


def getNextCell(sgrid):
    for row in range(9):
        for col in range(9):
            if sgrid[row][col] == 0:
                return row, col
    return -1


def isRowValid(sgrid, row, num):
    for item in sgrid[row]:
        if item == num:
            return False
    return True


def isColValid(sgrid, col, num):
    for row in range(9):
        if sgrid[row][col] == num:
            return False
    return True


def isBoxValid(sgrid, row, col, num):
    row, col = 3*(row//3), 3*(col//3)      #   top left corner of box
    for x in range(3):
        for y in range(3):
            if sgrid[row + x][col + y] == num:
                return False
    return True


def isCellValid(sgrid, row, col, num):
    return isRowValid(sgrid, row, num) and isColValid(sgrid, col, num) and isBoxValid(sgrid, row, col, num)


def solvePuzzle(sgrid):
    curCell = getNextCell(sgrid)
    if curCell == -1:
        return sgrid

    for num in range(1, 10):
        if isCellValid(sgrid, curCell[0], curCell[1], num):
            sgrid[curCell[0]][curCell[1]] = num
            recurseSolve = solvePuzzle(sgrid)
            if recurseSolve != -1:  # if found return grid
                return sgrid
            sgrid[curCell[0]][curCell[1]] = 0
    return -1       # if all tracks iterated, return -1


def printSolved(sgrid):
    for row in sgrid:
        for val in row:
            print(val, end=' ')
        print()


def main():
    while True:
        gridFile = input("Enter Input File: ")
        try:
            ogridFile = open(gridFile)
            break
        except Exception:
            print("Error Opening File, Please Try Again\n")

    sgrid = []   # initialize grid

    for row in ogridFile:
        row = row.split()
        sgrid.append(list(map(int, row)))   #sgrid is the sudoku table, turn all values into integers

    sgrid = solvePuzzle(sgrid)
    if sgrid == -1:
        print("No Solution")
    else:
        printSolved(sgrid)


if __name__ == "__main__":
    main()
