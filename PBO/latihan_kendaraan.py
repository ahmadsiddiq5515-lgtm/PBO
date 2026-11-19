class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk} ({self.tahun}) - Warna: {self.warna}, Bahan Bakar: {self.bahan_bakar}"

k1 = Kendaraan("Toyota Avanza", "Hitam", 2022)
k2 = Kendaraan("Honda Beat", "Merah", 2024)

# Perbedaan akses class attribute vs instance attribute
print("Akses class attribute via class:", Kendaraan.bahan_bakar)
print("Akses instance attribute k1:", k1.merk, k1.warna, k1.tahun)
print("Akses instance attribute k2:", k2.merk, k2.warna, k2.tahun)

# Mengubah class attribute pada class memengaruhi objek yang belum meng-override
Kendaraan.bahan_bakar = "Pertamax"
print("Setelah diubah di class -> k1:", k1.info_kendaraan())
print("Setelah diubah di class -> k2:", k2.info_kendaraan())

# Mengubah atribut khusus pada instance k2 saja
k2.bahan_bakar = "Listrik"
print("Setelah k2 di-override -> k1:", k1.info_kendaraan())
print("Setelah k2 di-override -> k2:", k2.info_kendaraan())