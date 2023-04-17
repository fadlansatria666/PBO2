# Nama  : Fadlan Satria Triswanto
# Kelas : D3
# NIM   : 210510001

class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "bergerak")
class Kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Meow!")
        
kucingA = Kucing("Sky", 1, "Persia")
kucingA.bergerak() 
kucingA.bersuara() 