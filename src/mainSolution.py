from matrix import Matrix
from point import Point
import math
import time

interval = 10000
iteration = 0

start = 0
end = 0

def solve(board:Matrix):    
    newBoard = copyBoard(board)
    for i in range(0,newBoard.rows):
        for j in range(0,newBoard.cols):
            if (i == j):
                newBoard.setElmnt(i,j,"#")
            else:
                newBoard.setElmnt(i,j,"0")
    M = bruteForce(board, newBoard, board.cols)

    if M is None:
        print(f"TIDAK ADA solusi yang ditemukan, max iteration: {iteration}\n")
        return None
    else:
        return M

def bruteForce(board:Matrix, copyBoard:Matrix, k):
    global iteration
    if (k == 1):
        iteration += 1
        return validate(board, copyBoard)
    
    M = bruteForce(board, copyBoard, k-1)
    if  M is not None:
        return M

    for i in range(0,k-1):
        if k % 2 == 0:
            swap(copyBoard, i, k-1)
        else:
            swap(copyBoard, 0, k-1)
        M = bruteForce(board, copyBoard, k-1)
        if M is not None:
            return M
    return None


def swap(board:Matrix, colA, colB):
    for i in range(0, board.rows):
        if board.getElmnt(i,colA) == "#":
            rowA = i
    for i in range(0,board.rows):
        if board.getElmnt(i,colB) == "#":
            rowB = i
    
    board.setElmnt(rowA, colA, "0")
    board.setElmnt(rowB, colB, "0")
    board.setElmnt(rowB, colA , "#")
    board.setElmnt(rowA, colB, "#")
    
def validate(board:Matrix, newBoard:Matrix):
    global end
    arrPoints = []
    count = 0
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

    if (colorCheck and digonalCheck):
        print("SUKSES pada ")
        end = time.perf_counter()
        displayBoard(checkBoard)
        return checkBoard
    else:
        if (iteration % interval == 0):
            end = time.perf_counter()
            displayBoard(checkBoard)
        return None

def copyBoard(board:Matrix):
    copyBoard = Matrix(board.rows, board.cols)
    for i in range(copyBoard.rows):
        for j in range(copyBoard.cols):
            copyBoard.setElmnt(i,j, board.getElmnt(i,j))
    return copyBoard


def displayBoard(board:Matrix):
    print("iterasi ke - " + str(iteration) + "\n")
    for i in range(board.rows):
        for j in range(board.cols):
            print(board.getElmnt(i,j), end=" ")
        print()
    print()

def countComplexity(n):
    return math.factorial(n)

# rows = int(input("Rows:\n"))
# cols = int(input("Col:\n"))

# M = Matrix(rows, cols)

# print(f"Masukkan {rows} baris, tiap baris berisi {cols} kolom:")
start = 0
end = 0
# for i in range(rows):
#     parts = input().split()
#     if len(parts) != cols:
#         print(f"Baris ke-{i} harus {cols} elemen, tapi dapat {len(parts)}")
#     for j in range(cols):
#         M.setElmnt(i, j, parts[j])

# print("jawaban\n")
# M = solve(M)



    

