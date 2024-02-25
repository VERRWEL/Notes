# TUGAS 1 PBO
# Menghitung gaji pegawai
# Varel gabriel wungow | 2PTI52 | 32230062
"""
membuat program menghitung gaji pegawai dengan class yang mempunyai method uang_makan()
yaitu 10% dari gaji, transport() yaitu 10% dari gaji, dan method total_gaji() yaitu
= gaji + uang_makan + transport
"""

class pegawai():
    def __init__(self):
        self.nik = int(input("masukkan NIK      : "))
        self.nama = str(input("masukkan Nama    :"))
        self.gaji = int(input("masukkan gaji    : "))
        print(f"\n|{self.nik} adalah nik",  f"{self.nama} adalah nama",f"{self.gaji:,} adalah gaji",sep='\t|')
    def uang_makan(self):
        self.makan = self.gaji * 0.10
    def transport(self):
        self.trans = self.gaji * 0.10
    def total_gaji(self):
        self.total = self.gaji + self.makan + self.trans
    def disp(self):
        print(self.total)

    
pegawai.disp