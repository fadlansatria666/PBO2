def calculate_factorial(n):
    if n < 0:
        raise ValueError("Nilai n harus non-negatif.")
    result = 1
    for i in range(1, n+1):
        result *= i
        if result > 10**100:
            raise OverflowError("Hasil faktorial terlalu besar untuk dihitung.")
    return result

try:
    factorial = calculate_factorial(1000)
    print("Faktorial:", factorial)
except OverflowError as e:
    print(e)
