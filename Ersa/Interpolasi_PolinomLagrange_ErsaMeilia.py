# Program interpolasi dengan metode Polinom Lagrange
# Nama : Ersa Meilia
# NIM : 2200458

def lagrange_interpolation(x_values, y_values, x_interpolate):
    n = len(x_values)
    
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x_interpolate - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Input nilai x dan y float
x_values = list(map(float, input("Masukkan nilai x (dipisahkan dengan spasi): ").split()))
# misal di inputkan x 8.0 9.0 9.5 
y_values = list(map(float, input("Masukkan nilai y (dipisahkan dengan spasi): ").split()))
# misal di inputkan y 2.079442 2.197225 2.251292

# Input nilai x yang ingin diinterpolasi
x_interpolate = float(input("Masukkan nilai x yang ingin diinterpolasi: "))
# misal di inputkan x 9.2

# Melakukan interpolasi dengan metode Polinom Lagrange
result_lagrange = lagrange_interpolation(x_values, y_values, x_interpolate)

# Menampilkan hasil interpolasi
print(f"Hasil interpolasi (Metode Polinom Lagrange) untuk x={x_interpolate}: {result_lagrange}")
