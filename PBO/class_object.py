class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"

# Pembuatan object
mhs1 = Mahasiswa("ahmad siddiq albasri", "202512045")
mhs2 = Mahasiswa("arya pratama", "202512046")

print(mhs1.perkenalan())
print(mhs2.perkenalan())