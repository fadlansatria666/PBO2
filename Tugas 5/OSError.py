import os

try:
    file = open("file_that_does_not_exist.txt", "r")
except OSError as e:
    print("Terjadi kesalahan sistem operasi:", e)
