# Nama  : Fitri Amalia Nurfathir
# Kelas : R1
# NIM   : 210511005

class Penulis:
    def __init__(self, name):
        self.name = name
        self.karya = Karya()
        print("Karya Raditya Dika")

class Judul:
    def __init__(self, name, tahun):
        self.name = name
        self.tahun = tahun

class Karya:
    def __init__(self):
        self.items = []
    
    def add_item1(self, item):
        self.items.append(item)
        print ("Judul: ", item.name, item.tahun)
    def add_item2 (self, item):
        self.items.append(item)
        print ("Judul: ", item.name, item.tahun)

    def remove_item(self, item):
        self.items.remove(item)

penulis = Penulis(" ")
judul1 = Judul("Cinta Brontosaurus", [2006])
judul2 = Judul("Memut Merah jambu", [2010])

print("="*40)
penulis.karya.add_item1(judul1)
penulis.karya.add_item2(judul2)
penulis.karya.items
print(" ")
