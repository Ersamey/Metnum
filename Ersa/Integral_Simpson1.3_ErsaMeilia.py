import math
# Program untuk menghitung integral menggunakan metode Simpson 1/3
# Nama: Ersa Meilia 
# NIM: 2200458 

def simpson_1_3(f, a, b, h):
    n = int((b - a) / h)

    if n % 2 != 0:
        raise ValueError("Jumlah subinterval harus genap untuk metode Simpson 1/3")

    result = f(a) + f(b)

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            result += 2 * f(x_i)
        else:
            result += 4 * f(x_i)

    return (h / 3) * result

# Input dari pengguna
a = float(input("masukan batas bawah integral (a): "))
b = float(input("masukan batas atas integral (b): "))
h = float(input("Masukkan nilai h (lebar subinterval): "))

# Meminta pengguna untuk memasukkan fungsi integrand
fungsi_input = input("Masukkan fungsi integrand f(x): ")
fungsi_input = fungsi_input.replace('e', str(math.e)) # gantikan nilai "e" dengan math.e
# Evaluasi string fungsi_input menjadi objek fungsi menggunakan fungsi eval
fungsi_integrasi = lambda x: eval(fungsi_input)

result = simpson_1_3(fungsi_integrasi, a, b, h)
print(f"Hasil integral menggunakan metode Pias (titik tengah): {result}")