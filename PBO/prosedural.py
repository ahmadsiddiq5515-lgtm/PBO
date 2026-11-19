def hitung_luas_persegi(sisi):
    return sisi * sisi


# Fungsi untuk menghitung keliling persegi
def hitung_keliling_persegi(sisi):
    return 4 * sisi


# Pemanggilan fungsi
sisi = 5

# Menghitung luas dan keliling
luas = hitung_luas_persegi(sisi)
keliling = hitung_keliling_persegi(sisi)

# Menampilkan hasil
print("=== PROGRAM PERSEGI (PROSEDURAL) ===")
print(f"Panjang sisi  : {sisi}")
print(f"Luas persegi  : {luas}")
print(f"Keliling      : {keliling}")
