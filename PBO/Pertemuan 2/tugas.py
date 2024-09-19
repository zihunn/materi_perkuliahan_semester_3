#Membuat Class
class Perpustakaan:

    def __init__(self, judul, penulis, tahun_terbit):

        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun_terbit

    def __str__(self):
        return f"{self.judul}, {self.penulis}, {self.tahun}"
    
    def updateTahun(self, tahun_update):
        self.tahun = tahun_update
        
buku_a = Perpustakaan("Buku A", "Lorem", 2020)
print(buku_a.__dict__)
buku_a.updateTahun(2021)
print(buku_a.__dict__)

buku_b = Perpustakaan("Buku B", "Ipsum", 2001)
print(buku_b.__dict__)
buku_b.updateTahun(2024)
print(buku_b.__dict__)