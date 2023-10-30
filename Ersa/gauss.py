import numpy as np
#gaus part 2

def Sulih_Mundur(A, b, n): #fungsi untuk menyulih mundur matriks A dan vektor b
    x = np.zeros(n)  # Inisialisasi vektor x dengan nilai awal 0.0

    x[n - 1] = b[n - 1] / A[n - 1, n - 1] # Hitung solusi x[n-1] atau x terakhir

    for k in range(n - 2, -1, -1): #n-2 sampai -1 dengan step -1
        sigma = 0 #inisialisasi sigma dengan nilai awal 0.0
        for j in range(k + 1, n): #k+1 sampai n
            sigma += A[k, j] * x[j] # Hitung sigma untuk solusi x[k]

        x[k] = (b[k] - sigma) / A[k, k] # Hitung solusi x[k]

    return x

def Eliminasi_Gauss(A, b, n):
    x = np.zeros(n)  # Inisialisasi vektor x dengan nilai awal 0.0 untuk menyimpan solusi
    #apakah matriks A memiliki singularitas atau tidak
    singular = False  # Inisialisasi variabel singular
    
    k = 0
    while k <= n - 1 and not singular:
        # Cari elemen pivot dengan nilai mutlak terbesar
        pivot = A[k, k] #diagonal utama baris k kolom k
        r = k  # menandai baris pivot

        for t in range(k + 1, n): #k+1 sampai n
            if abs(A[t, k]) > abs(pivot): #jika elemen di bawah diagonal utama lebih besar dari pivot
                pivot = A[t, k]  # update nilai pivot
                r = t #update baris pivot

        # Jika pivot=0 maka matriks A singular
        if pivot == 0: #jika pivot = 0
            singular = True # Matriks A singular
        else: #jika pivot != 0
            if r > k: # Jika baris pivot tidak sama dengan baris k, maka tukar baris
                # Pertukarkan baris k dengan baris r di matriks A
                A[[k, r]] = A[[r, k]]

                # Pertukarkan juga b[k] dengan b[r]
                b[k], b[r] = b[r], b[k]

            for i in range(k + 1, n): #k+1 sampai n
                m = A[i, k] / A[k, k]  # Hitung faktor pengali
                A[i, k:n] = A[i, k:n] - m * A[k, k:n]  # Eliminasi baris i dari kolom k sampai kolom n
                b[i] = b[i] - m * b[k]  # Eliminasi vektor b pada baris i

        k += 1 #increment untuk while k <= n - 1

    if not singular: # Jika matriks A tidak singular, maka solusi ada
        x = Sulih_Mundur(A, b, n)  # Dapatkan solusi dengan teknik penyulihan mundur
    else: 
        # Solusi tidak ada, tetapi vektor x harus tetap diisi dengan -9999
        x = np.full(n, -9999)

    return x 

# Meminta input matriks A dari pengguna
n = int(input("Masukkan ukuran matriks (n x n): "))
A = np.zeros((n, n)) #inisialisasi matriks A dengan nilai awal 0.0
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n): 
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1}][{j+1}]: ")) #input elemen matriks A

# Meminta input matriks b dari pengguna
b = np.zeros(n) #inisialisasi vektor b dengan nilai awal 0.0
print("Masukkan elemen-elemen vektor b:")
for i in range(n):
    b[i] = float(input(f"B[{i+1}]: "))

solusi = Eliminasi_Gauss(A, b, n) #panggil fungsi Eliminasi_Gauss untuk membuat 0 di bawah diagonal utama atau 9999 jika tidak ada solusi

if -9999 in solusi: #jika ada 9999 di dalam solusi
    print('Solusi tidak ada (atau tidak unik)') #maka solusi tidak ada
else: #jika tidak ada 9999 di dalam solusi
    print('Solusi:') #maka solusi ada
    #print solusi
    for i, val in enumerate(solusi): 
        print(f"x{i+1} = {val}")
