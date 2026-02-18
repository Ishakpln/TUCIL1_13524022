from matrix import Matrix
import os

def parse(path:str):
    fullpath = "../Input/" + path + ".txt"

    if not os.path.exists(fullpath):
        print(f"File tidak ditemukan: {fullpath}")
        return None

    rowsL = []
    with open(fullpath, "r", encoding="utf-8") as file:
        for row in file:
            row = row.strip()
            if not row:
                continue
            if " " in row:
                rowsL.append(row.split())
            else:
                rowsL.append(list(row))

    if (len(rowsL)) == 0:
        print("Input board kosong")
        return None
    
    rows = len(rowsL)
    cols = len(rowsL[0])

    if (rows != cols):
        print("board tidak persegi sempurna")
        return None
    
    if (rows == 0 or cols == 0):
        print("Input board kosong")
        return None

    x = len(rowsL[0])
    for i in range(rows):
        if x != len(rowsL[i]):
            print("board tidak persegi sempurna")
            return  None        

    colors = []
    countColors = 0
    for i in range(rows):
        for j in range(cols):
            if rowsL[i][j] in colors:
                continue                
            else:
                countColors += 1
                colors.append(rowsL[i][j])

    if countColors != rows and countColors != cols:
        print("board mimiliki jumlah warna yang tidak sama dengan baris atau kolom")
        return None
        
    M = Matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            M.setElmnt(i,j,rowsL[i][j])
    return M

    
