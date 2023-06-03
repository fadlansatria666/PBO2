# Nama  : Fadlan Satria Triswanto
# Kelas : R1
# NIM   : 210510001

def divide(a, b):
    assert b != 0, "Pembagian dengan nol tidak dapat dilakukan."
    return a / b

print(divide(10, 0))
# Output:
# AssertionError: Pembagian dengan nol tidak dapat dilakukan.