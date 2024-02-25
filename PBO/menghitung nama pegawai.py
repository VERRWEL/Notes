# TUGAS 1 PBO
# Menghitung gaji pegawai
# Varel gabriel wungow | 2PTI52 | 32230062
"""
membuat program menghitung gaji pegawai dengan class yang mempunyai method uang_makan()
yaitu 10% dari gaji, transport() yaitu 10% dari gaji, dan method total_gaji() yaitu
= gaji + uang_makan + transport
"""
nik     = int(input("masukkan nik : "))
nama    = input("masukkan nama : ")
gaji    = int(input("masukkan gaji : "))

class pegawai():
    def __init__(self,nik,gaji,nama):
        self.nik = nik
        self.nama = nama
        self.gaji = gaji
    
    def makan(self):            #method uang_makan()
        mkn = self.gaji * 0.10
        return mkn
    
    def trns(self):             #method transport()
        trs = self.gaji * 0.10
        return trs
    
    def total(self):            #method total_gaji()
        tg = self.gaji + self.makan() + self.trns()
        return tg 

p = pegawai(nik,gaji,nama)
string = f"{p.total():,}"
print(string, "adalah total gaji bersih anda")



