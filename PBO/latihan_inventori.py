class ManajerInventori:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.inventori = {}  # format: {nama_barang: stok}

    def tambah_barang(self, nama_barang, jumlah):
        if jumlah <= 0:
            return "Jumlah penambahan barang harus lebih dari 0."
        self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
        return f"Stok '{nama_barang}' ditambah {jumlah}. Total stok: {self.inventori[nama_barang]}"

    def hapus_barang(self, nama_barang, jumlah=None):
        if nama_barang not in self.inventori:
            return f"Barang '{nama_barang}' tidak ditemukan di inventori."

        # Jika jumlah tidak disebutkan, hapus item dari inventori
        if jumlah is None:
            del self.inventori[nama_barang]
            return f"Item '{nama_barang}' dihapus dari inventori."

        if jumlah <= 0:
            return "Jumlah pengurangan harus lebih dari 0."
        if jumlah > self.inventori[nama_barang]:
            return f"Stok '{nama_barang}' tidak cukup (tersisa {self.inventori[nama_barang]})."

        self.inventori[nama_barang] -= jumlah
        if self.inventori[nama_barang] == 0:
            del self.inventori[nama_barang]
            return f"Stok '{nama_barang}' habis dan dihapus dari daftar."
        return f"Stok '{nama_barang}' dikurangi {jumlah}. Sisa stok: {self.inventori[nama_barang]}"

    def lihat_inventori(self):
        if not self.inventori:
            return f"Inventori {self.nama_toko} kosong."
        hasil = [f"=== Inventori {self.nama_toko} ==="]
        for barang, stok in self.inventori.items():
            hasil.append(f"- {barang}: {stok} unit")
        return "\n".join(hasil)

# Demonstrasi semua method
toko = ManajerInventori("Toko Sumber Rejeki")
print(toko.tambah_barang("Buku Tulis", 20))
print(toko.tambah_barang("Pulpen", 15))
print(toko.tambah_barang("Buku Tulis", 10))
print(toko.hapus_barang("Pulpen", 5))
print(toko.lihat_inventori())
print(toko.hapus_barang("Buku Tulis", 30))
print(toko.lihat_inventori())