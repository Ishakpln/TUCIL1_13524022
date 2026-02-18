class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = [["." for _ in range(rows)] for _ in range(cols)]

    def getElmnt(self, i, j):
        return self.elements[i][j]
    
    def setElmnt(self, i, j, value):
        self.elements[i][j] = value
