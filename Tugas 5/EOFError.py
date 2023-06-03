# Nama  : Fadlan Satria Triswanto
# Kelas : R1
# NIM   : 210510001

try:
    user_input = input("Masukkan sesuatu: ")
    print("Input yang dimasukkan:", user_input)
except EOFError:
    print("Terjadi EOFError. Input tidak ditemukan.")
