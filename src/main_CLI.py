from loader import *
from save import *
import mainSolution
import solution
import time

def main(): 
    tryAgain = 0
    print("Selamat datang di QueenSolver!")
    print("Play? (Ya/Tidak)")
    choiceF = str(input())
    
    while choiceF != "Ya" and choiceF != "Tidak":
        print("Input TIDAK VALID")
        print("Play? (Ya/Tidak)")
        choiceF = str(input())

    if choiceF == "Ya":
        tryAgain = 1
    elif choiceF == "Tidak":
        tryAgain = 0

    while (tryAgain):
        print("Pilih nama file board yang ingin di solved DI FOLDER Input!")
        path = str(input("nama file: "))
        M = parse(path)

        if M is None:
            continue

        mainSolution.iteration = 0
        solution.iteration = 0
        
        print("Pilih metode algoritma (1) atau (2): ")
        print("Algoritma (1): Constrained brute force: O(N!)")
        print("Algoritma (2): Blind brute force: O(N^(2N))")
        choice = int(input())

        while choice != 1 and choice != 2:
            print("Input TIDAK VALID")
            print("Pilih metode algoritma (1) atau (2): ")
            print("Algoritma (1): Constrained brute force: O(N!)")
            print("Algoritma (2): Blind brute force: O(N^(2N))")
            choice = int(input())

        print("Masukkan interval percobaan solusi yang akan ditampilkan: ")
        print("CATATAN: sebaiknya interval >1000 agar execution time sedikit dipengaruhi oleh I/O lag")
        intv = int(input())
        if choice == 1:
            mainSolution.interval = intv
            start = time.perf_counter()
            Ms = mainSolution.solve(M)
            end = time.perf_counter()
            cases = mainSolution.iteration
        elif choice == 2:
            solution.interval = intv
            start = time.perf_counter()
            Ms = solution.solve(M)
            end = time.perf_counter()
            cases = solution.iteration
            
        print(f"Waktu pencarian solusi: {(end-start)*1000} ms ")
        print(f"Banyak kasus yang ditinjau: {cases}")
        print(f"Apakah anda ingin menyimpan solusi? (Ya/Tidak)")
        choice2 = str(input())

        while choice2 != "Ya" and choice2 != "Tidak":
            print("Input TIDAK VALID")
            print(f"Apakah anda ingin menyimpan solusi? (Ya/Tidak)")
            choice2 = str(input())

        if choice2 == "Ya":
            print("Masukkan nama file: ")
            pathS = str(input())
            save(pathS, Ms)
            print("Berhasil disimpan di folder Test")
        
        print("Coba lagi? (Ya/Tidak)")
        choice3 = str(input())
        while (choice3 != "Ya" and choice3 != "Tidak"):
            print("Input TIDAK VALID")
            print("Coba lagi? (Ya/Tidak)")
            choice3 = str(input())

        if choice3 == "Ya":
            continue
        else:
            tryAgain = 0
    

if __name__ == "__main__":
    main()



