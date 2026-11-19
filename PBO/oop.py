# Membuat class Persegi
class Persegi:

    # Constructor untuk menerima nilai sisi
    def __init__(self, sisi):
        self.sisi = sisi

    # Method untuk menghitung luas
    def hitung_luas(self):
        return self.sisi * self.sisi

    # Method untuk menghitung keliling
    def hitung_keliling(self):
        return 4 * self.sisi


# Membuat object dari class Persegi
persegi = Persegi(5)

# Menampilkan hasil perhitungan
print("=== PROGRAM PERSEGI (OOP) ===")
print(f"Panjang sisi  : {persegi.sisi}")
print(f"Luas persegi  : {persegi.hitung_luas()}")
print(f"Keliling      : {persegi.hitung_keliling()}")