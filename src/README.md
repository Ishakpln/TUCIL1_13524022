Penyelesaian Permainan Queens Linkedin Dengan Menggunakan Algoritma Brute Force
Tugas Kecil 1 = IF2211 Strategi Algoritma
Semester II 2025/2026

a. Penjelasan Singkat Program
Algoritma solver dibuat murni dengan menggunakan algoritma brute force
Flow program:

1. Membaca file .txt
2. Validasi input
3. Mencari solusi dengan menggunakan algoritma brute force
4. Menampilkan banyak percobaan yagn ditinjau , waktu pencarian dalam ms, live updat proses brute force yang ditampilkan berdasarkan interval input

Porgram mengimplementasikan 2 algoritma brute force yaitu

1. Constrained Brute Force (O(N!))
   Algoritma ini memberikan constraint pada setiap iterasi sehingga tidak ada dua atau lebih queen yang berada pada baris atau kolom yang sama. Papan dimulai dengan menempatkan seluruh queen secara diagonal dari kiri atas ke kanan bawah.
2. Blind Brute Force (O(N^(2N)))
   Algoritma ini bekerja hanya secara buta menempatkan semau queen pada tiap sel di dalam board tanpa adanya constraint apa pun. Board dimulai dengan menempatkan semua queen secara berjejer di kiri atas papan, kemudian setiap iterasi, tiap queen akan dipindah board tiap langkah mirip seperti cara kerja odometer

b. Requirement dan Instalasi

1. Python 3.8 atau lebih baru
2. Tidak memerlukan library external tambahan

c. Cara Compile Program

Program ditulis dalam Python sehingga tidak memerlukan proses kompilasi

d. Cara Menjalankan Program

1. masuk ke file src
2. jalankan python main_CLI.py
3. ikuti instruksi pada terminal

CATATAN:
Pastikan input .txt board berada di file Input
