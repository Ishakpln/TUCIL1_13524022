from matrix import Matrix
from point import Point
import math
import time

interval = 1000
iteration = 0

def solve(board:Matrix):
    newBoard = Matrix(board.rows, board.cols)
    for i in range(newBoard.rows):
        for j in range(newBoard.cols):
            newBoard.setElmnt(i, j, "0")

    M = bruteForce(board, newBoard, board.cols)

    if M is None:
        print(f"TIDAK ADA solusi yang ditemukan, max iteration: {iteration}\n")
        return None
    else:
        return M
    
def bruteForce(board: Matrix, newBoard: Matrix, N: int):
    global iteration
    cells = newBoard.rows * newBoard.cols

    if N > cells:
        return None

    pos = [i for i in range(N)]

    used = [False] * cells
    for p in pos:
        used[p] = True

    while True:

        clearnewBoard(newBoard)   

        for p in pos:
            row = p // newBoard.cols
            col = p % newBoard.cols
            newBoard.setElmnt(row, col, "#")


        iteration += 1
        M = validate(board, newBoard)
        if M is not None:
            return M

        if not increment_positions(pos, used, N, cells):
            break

    return None


def increment_positions(pos, used, N, cells):
    k = N - 1
    while k >= 0:
        used[pos[k]] = False

        nxt = pos[k] + 1
        while nxt < cells and used[nxt]:
            nxt += 1

        if nxt < cells:
            pos[k] = nxt
            used[nxt] = True

            for t in range(k + 1, N):
                x = 0
                while x < cells and used[x]:
                    x += 1
                if x >= cells:
                    return False
                pos[t] = x
                used[x] = True

            return True

        else:
            k -= 1

    return False


def clearnewBoard(newBoard: Matrix):
    for i in range(newBoard.rows):
        for j in range(newBoard.cols):
            newBoard.setElmnt(i, j, "0")



def validate(board:Matrix, newBoard:Matrix):
    global end
    arrPoints = []
    count = 0
    rowColCheck = 1
    colorCheck = 1
    digonalCheck = 1

    checkBoard = copyBoard(board)
    for i in range(board.rows):
        for j in range(board.cols):
            if newBoard.getElmnt(i,j) == "#":
                p = Point(i,j,board.getElmnt(i,j))
                arrPoints.append(p)
                checkBoard.setElmnt(i,j,"#")
                count += 1

    #check row-col
    for i in range(board.rows):
        thisRowExist = 0
        for j in range(board.cols):
            if checkBoard.getElmnt(i,j) == "#":
                thisRowExist += 1
            if thisRowExist > 1:
                rowColCheck = 0
                break
        if rowColCheck == 0:
            break
    for i in range(board.cols):
        thisColExist = 0
        for j in range(board.rows):
            if checkBoard.getElmnt(j,i) == "#":
                thisColExist += 1
            if thisColExist > 1:
                rowColCheck = 0
                break
        if rowColCheck == 0:
            break
        
    #check color similarities
    check  = []
    for i in range(0,count):
        if arrPoints[i].color in check:
            colorCheck = 0
        else:
            check.append(arrPoints[i].color)

    #check diagonal
    for i in range(board.rows):
        for j in range(board.cols):
            if checkBoard.getElmnt(i,j) == "#":
                if (i+1) <= board.rows-1 and (j+1) <= board.cols-1 and checkBoard.getElmnt(i+1,j+1) == "#":
                    digonalCheck = 0
                    break
                if (i+1) <= board.rows-1 and (j-1) >= 0 and checkBoard.getElmnt(i+1,j-1) == "#":
                    digonalCheck = 0
                    break
        if not digonalCheck:
            break

    if (rowColCheck and colorCheck and digonalCheck):
        print("SUKSES pada ")
        end = time.perf_counter()
        displayBoard(checkBoard)
        return checkBoard
    else:
        if (iteration % interval == 0):
            end = time.perf_counter()
            displayBoard(checkBoard)
        return None
    
def displayBoard(board:Matrix):
    print("iterasi ke - " + str(iteration) + "\n")
    for i in range(board.rows):
        for j in range(board.cols):
            print(board.getElmnt(i,j), end=" ")
        print()
    print()


    
def copyBoard(board:Matrix):
    copyBoard = Matrix(board.rows, board.cols)
    for i in range(copyBoard.rows):
        for j in range(copyBoard.cols):
            copyBoard.setElmnt(i,j, board.getElmnt(i,j))
    return copyBoard
