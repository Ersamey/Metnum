def trapesium(a, b, n, f):
    h = (b - a) / n  # lebar pias
    print("lebar pias (h):", h)
    x = a  # awal selang integrasi
    I = f(a) + f(b)
    print("f(a) + f(b):", I)
    sigma = 0

    for _ in range(1, n):
        x = x + h
        print("x ke-", _, ":", x)
        sigma = sigma + 2 * f(x)

    I = (I + sigma) * h / 2  # nilai integrasi numerik
    return I

a = float(input("masukan batas bawah integral (a): "))
b = float(input("masukan batas atas integral (b): "))
n = int(input("masukan banyak interval (n): "))

expression = input("Masukkan fungsi f(x): ") # Input fungsi dari pengguna
f = lambda x: eval(expression)

result = trapesium(a, b, n, f) # Memanggil fungsi trapesium
print("Hasil integral numerik:", result)