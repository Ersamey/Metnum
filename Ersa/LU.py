import numpy as np
#LU
def jalanLU(A,b): #fungsi untuk menyulih mundur matriks A dan vektor b
    n = len(A) #ukuran matriks A
    L = np.zeros((n,n)) #matriks L
    for i in range(n): #perulangan untuk membuat matriks L
        L[i][i] = 1

    for k in range(n-1): #perulangan untuk membuat matriks U
        if A[k][k] == 0: #jika elemen diagonal utama = 0 
            for s in range(n): #perulangan untuk menukar baris
                v = A[k][s] #simpan elemen baris k kolom s
                u = A[k+1][s]  #simpan elemen baris k+1 kolom s
                A[k][s] = u #tukar elemen baris k kolom s dengan elemen baris k+1 kolom s 
                A[k+1][s] = v #tukar elemen baris k+1 kolom s dengan elemen baris k kolom s

        for j in range(k+1,n): #perulangan untuk membuat matriks L
            m = A[j][k]/A[k][k] #hitung faktor pengali 
            L[j][k] = m #simpan faktor pengali di matriks L 
            for i in range(n): #perulangan untuk membuat matriks U 
                A[j][i] = A[j][i] - m*A[k][i] #hitung elemen matriks U 

    print('Matriks L') 
    print(L)

    print('Matriks U')
    print(A)

    y = np.zeros((n,1)) #vektor y
    y[0][0] = b[0][0]/L[0][0] #hitung elemen pertama vektor y
    for j in range(1,n): #perulangan untuk menyulih mundur vektor y 
        S = 0 
        for i in range(j): 
            S = S + y[i][0]*L[j][i] 
        y[j][0] = b[j][0] - S 

    x = np.zeros((n,1)) #vektor x
    x[n-1][0] = y[n-1][0]/A[n-1][n-1] #hitung elemen terakhir vektor x
    for j in range(n-2,-1,-1): #perulangan untuk menyulih mundur vektor x
        S = 0
        for i in range(j+1,n):
            S = S + A[j][i]*x[i][0]
        x[j][0] = (y[j][0] - S)/A[j][j]

    print('Solusi:\n') 
    for i in range(n):
        print(f'X{i+1} = {x[i]}')

# Meminta input matriks A dari pengguna
A = [] #definisikan matriks A
n = int(input("Masukkan ukuran matriks (n x n): "))
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    row = [] 
    for j in range(n):
        elem = float(input(f"A[{i+1}][{j+1}]: "))
        row.append(elem) #tambahkan elemen ke dalam baris
    A.append(row) #tambahkan baris ke dalam matriks A

# Meminta input matriks b dari pengguna
b = [] #definisikan vektor b
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elem = float(input(f"B[{i+1}]: "))
    b.append([elem]) #tambahkan elemen ke dalam vektor b

# Memanggil fungsi jalanLU dengan matriks A dan b yang dimasukkan oleh pengguna
jalanLU(np.array(A), np.array(b)) 