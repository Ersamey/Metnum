import math
# Program untuk menghitung integral menggunakan metode titik tengah (Pias)
# Nama: Ersa Meilia 
# NIM: 2200458 

def titik_tengah(f, a, b, h):
    n = int((b - a) / h)
    result = 0

    for i in range(1, n + 1):
        x_i = a + (i - 0.5) * h
        result += f(x_i)

    return h * result

# Input dari pengguna
a = float(input("masukan batas bawah integral (a): "))
b = float(input("masukan batas atas integral (b): "))
h = float(input("Masukkan nilai h (lebar subinterval): "))

# Meminta pengguna untuk memasukkan fungsi integrand
fungsi_input = input("Masukkan fungsi integrand f(x): ")
fungsi_input = fungsi_input.replace('e', str(math.e)) # gantikan nilai "e" dengan math.e
# Evaluasi string fungsi_input menjadi objek fungsi menggunakan fungsi eval
fungsi_integrasi = lambda x: eval(fungsi_input)

result = titik_tengah(fungsi_integrasi, a, b, h)
print(f"Hasil integral menggunakan metode Pias (titik tengah): {result}")