# Nama  : Fadlan Satria Triswanto
# Kelas : D3
# NIM   : 210510001

class Peneliti:
    def __init__(self, name):
        self.name = name
        self.judul = Judul()
        print("fitri")

class Jurnal:
    def __init__(self, name):
        self.name = name

class Judul:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print ("Judul Jurnal: ", item.name)

    def remove_item(self, item):
        self.items.remove(item)

peneliti = Peneliti(" ")
jurnal1 = Jurnal("Sistem")
jurnal2 = Jurnal("Informasi")

print("="*40)
peneliti.judul.add_item(jurnal1)
peneliti.judul.add_item(jurnal2)
peneliti.judul.items
print(" ")
