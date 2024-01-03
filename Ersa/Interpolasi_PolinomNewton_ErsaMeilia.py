# Program interpolasi polinom Newton
# Nama : Ersa Meilia
# NIM : 2200458

def newton_interpolation(x_values, y_values, x_interpolate):
    n = len(x_values)
    coefficients = y_values.copy()

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            coefficients[j] = (coefficients[j] - coefficients[j - 1]) / (x_values[j] - x_values[j - i])

    result = coefficients[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_interpolate - x_values[i]) + coefficients[i]

    return result

# Input nilai x dan y float
x_values = list(map(float, input("Masukkan nilai x (dipisahkan dengan spasi): ").split()))
# misal di inputkan x 8.0 9.0 9.5 
y_values = list(map(float, input("Masukkan nilai y (dipisahkan dengan spasi): ").split()))
# misal di inputkan y 2.079442 2.197225 2.251292

# Input nilai x yang ingin diinterpolasi
x_interpolate = float(input("Masukkan nilai x yang ingin diinterpolasi: "))
# misal di inputkan x 9.2

# Melakukan interpolasi dengan metode Polinom Newton
result_newton = newton_interpolation(x_values, y_values, x_interpolate)

# Menampilkan hasil interpolasi
print(f"Hasil interpolasi (Metode Polinom Newton) untuk x={x_interpolate}: {result_newton}")
