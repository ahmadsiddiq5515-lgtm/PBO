class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor dengan default ipk=0.0
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        return (
            f"Halo, nama saya {self.nama}, NIM {self.nim}, "
            f"jurusan {self.jurusan} di {self.universitas}, dengan IPK saat ini {self.ipk:.2f}."
        )

    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            return f"IPK {self.nama} diperbarui menjadi {self.ipk:.2f}."
        return "IPK tidak valid (harus berada di rentang 0.0 - 4.0)."

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Belum Memenuhi Predikat Kelulusan"


# Instansiasi 3 object mahasiswa dengan data berbeda
mhs_a = Mahasiswa("Ahmad Siddiq", "202512045", "Teknik Informatika", 3.65)
mhs_b = Mahasiswa("Nadia Putri", "202512050", "Bisnis Digital", 3.10)
mhs_c = Mahasiswa("Rizky Pratama", "202512055", "Teknik Informatika")  # default ipk=0.0

daftar_mahasiswa = [mhs_a, mhs_b, mhs_c]

for mhs in daftar_mahasiswa:
    print(mhs.perkenalan_diri())
    print("Predikat awal:", mhs.predikat_kelulusan())

print("\n--- Update IPK ---")
print(mhs_c.update_ipk(2.75))
print(f"Predikat {mhs_c.nama} setelah update:", mhs_c.predikat_kelulusan())
print(mhs_b.update_ipk(3.55))
print(f"Predikat {mhs_b.nama} setelah update:", mhs_b.predikat_kelulusan())