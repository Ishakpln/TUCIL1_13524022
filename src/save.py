from matrix import Matrix

def save(path:str, board:Matrix):
    with open("../Test/" + path + ".txt", "w", encoding="utf-8") as file:
        if board is None:
            file.write("Tidak ADA SOLUSI")
        else:
            for i in range(board.rows):
                for j in range(board.cols):
                    file.write(str(board.getElmnt(i,j)))
                file.write("\n")

