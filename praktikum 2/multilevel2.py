# Nama  : Fadlan Satria Triswanto
# Kelas : D3
# NIM   : 210510001

class Buah:
    def __init__(self, name):
        self.name = name
    def Rasa(self):
        print("Buah-buahan memiliki banyak manfaat")

class Mangga(Buah):
    def __init__(self, name, rasa):
        super().__init__(name)
        self.rasa = rasa
    def Rasa(self):
        print("Mangga mengandung vitamin A")

class ManggaCengkir(Mangga):
    def __init__(self, name, rasa, asal):
        super().__init__(name, rasa)
        self.asal = asal
    def Rasa(self):
        print("Mangga Cengkir memiliki rasa yang manis")

ManggaCengkirA = ManggaCengkir("Mangga Cengkir"," manis", "Indonesia")
ManggaB = Mangga("Mangga", "Manis")
buahC = Buah("Buah apa yang enak?")
ManggaCengkirA.Rasa()
ManggaB.Rasa()
buahC.Rasa()