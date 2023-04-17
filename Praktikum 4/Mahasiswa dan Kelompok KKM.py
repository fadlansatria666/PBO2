# Nama  : Fadlan Satria Triswanto
# Kelas : D3
# NIM   : 210510001

class Mahasiswa:
    def __init__(self, name):
        self.name = name
        self.anggota = Anggota()
        print("Daftar Nama Mahasiswa Kelompok KKM")

class Kelompok_KKM:
    def __init__(self, name):
        self.name = name

class Anggota:
    def __init__(self):
        self.items = []
    
    def add_item1(self, item):
        self.items.append(item)
        print("Kelompok 1: ", item.name)
    def add_item2(self, item):
        print("Kelompok 2: ", item.name)
    
    def remove_item(self, item):
        self.items.remove(item)

mahasiswa = Mahasiswa(" ")
kel1 = Kelompok_KKM("Hore")
kel2 = Kelompok_KKM("Skuy")

print("="*40)
mahasiswa.anggota.add_item1(kel1)
mahasiswa.anggota.add_item2(kel2)
mahasiswa.anggota.items
print(" ")
