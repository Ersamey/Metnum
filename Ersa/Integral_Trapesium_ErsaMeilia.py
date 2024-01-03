import math
# Program untuk menghitung integral menggunakan metode trapesium
# Nama: Ersa Meilia 
# NIM: 2200458 

def trapesium(f, a, b, h):
    # hitung jumlah subinterval
    n = int((b - a) / h)
    result = f(a) + f(b) 

    for i in range(1, n):
        x_i = a + i * h 
        result += 2 * f(x_i)

    return (h / 2) * result

# Input dari pengguna
a = float(input("masukan batas bawah integral (a): "))
b = float(input("masukan batas atas integral (b): "))
h = float(input("Masukkan nilai h (lebar subinterval): "))

# Meminta pengguna untuk memasukkan fungsi integrand
fungsi_input = input("Masukkan fungsi integrand f(x): ")
fungsi_input = fungsi_input.replace('e', str(math.e)) # gantikan nilai "e" dengan math.e
# Evaluasi string fungsi_input menjadi objek fungsi menggunakan fungsi eval
fungsi_integrasi = lambda x: eval(fungsi_input)

result = trapesium(fungsi_integrasi, a, b, h)
print(f"Hasil integral menggunakan metode trapesium: {result}")