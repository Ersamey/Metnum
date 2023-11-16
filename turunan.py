# Fungsi untuk menghitung turunan pertama dengan pendekatan selisih-maju
def fAksen_maju(f0, fx1, h):
    return (fx1 - f0) / h

# Fungsi untuk menghitung turunan pertama dengan pendekatan selisih-mundur
def fAksen_mundur(f0, fx_1, h):
    return (f0 - fx_1) / h

# Fungsi untuk menghitung turunan pertama dengan pendekatan selisih-pusat
def fAksen_pusat(f1, f_1, h):
    return (f1 - f_1) / (2 * h)

# Lakukan perulangan menu
while True:
 # menampilkan menu pilihan metode
 print("Pilih metode:")
 print("1. Selisih Maju")
 print("2. Selisih Mundur")
 print("3. Selisih Pusat")
 print("4. Keluar")
 metode = int(input("Masukkan pilihan: "))
 if metode == 1:
  print("Metode yang dipilih: Selisih Maju")
  # input x0, f(x0), dan h
  x0 = float(input("Masukkan x0: "))
  fx0 = float(input("Masukkan f(x0): "))
  h = float(input("Masukkan h: "))
  # input x1 dan f(x1)
  x1 = float(input("Masukkan x1: "))
  fx1 = float(input("Masukkan f(x1): "))
  # hitung turunan pertama dengan pendekatan selisih-maju
  fAksen = fAksen_maju(fx0, fx1, h)
  # tampilkan hasil
  print("f'(x) = ", fAksen)
 elif metode == 2:
  print("Metode yang dipilih: Selisih Mundur")
  # input x0, f(x0), dan h
  x0 = float(input("Masukkan x0: "))
  fx0 = float(input("Masukkan f(x0): "))
  h = float(input("Masukkan h: "))
  # input x1 dan f(x1)
  x_1 = float(input("Masukkan x-1: "))
  fx_1 = float(input("Masukkan f(x-1): "))
  # hitung turunan pertama dengan pendekatan selisih-mundur
  fAksen = fAksen_mundur(fx0, fx_1, h)
  # tampilkan hasil
  print("f'(x) = ", fAksen)
 elif metode == 3:
  print("Metode yang dipilih: Selisih Pusat")
  # input x1, f(x1), dan h
  x1 = float(input("Masukkan x1: "))
  fx1 = float(input("Masukkan f(x1): "))
  h = float(input("Masukkan h: "))
  # input x_1 dan f(x_1)
  x_1 = float(input("Masukkan x-1: "))
  fx_1 = float(input("Masukkan f(x-1): "))
  # hitung turunan pertama dengan pendekatan selisih-pusat
  fAksen = fAksen_pusat(fx1, fx_1, h)
  # tampilkan hasil
  print("f'(x) = ", fAksen)
 elif metode == 4:
  break
