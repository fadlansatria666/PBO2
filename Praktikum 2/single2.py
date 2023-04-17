# Nama  : Fadlan Satria Triswanto
# Kelas : D3
# NIM   : 210510001

class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan ini sedang berjalan.")
class Mobil(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
        print("Mobil ini sedang belok.")

motorA = Mobil("Mobil", "Minibus", "Hitam", 2000)
motorA.berkendara() 
motorA.belok() 