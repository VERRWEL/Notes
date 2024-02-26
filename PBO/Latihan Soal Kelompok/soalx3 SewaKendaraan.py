"""
membuat program sewa kendaraan yang mempunyai methods:
- TotalSewa() yaitu LamaSewa*BiayaSewa
- PotonganHarga() yang menghitung potongan harga dengan beberapa kemungkinan yaitu :
jika LamaSewa >=
7 hari maka PotonganHarga 5%
dari TotalSewa, jika LamaSewa >= 5
hari maka PotonganHarga 3% dari
TotalSewa, jika LamaSewa >= 3 hari
maka PotonganHarga 2% dari
TotalSewa, jika LamaSewa <= 2 hari
maka PotonganHarga 0.
- ppn() yang menambahkan 2% dari TotalSewa
- HarusBayar() yaitu TotalSewa - PotonganHarga() + ppn()
"""

idpenyewa = str(input("masukkan ID anda\t: "))
nama = str(input("masukkan nama anda\t: "))
alamat = str(input("masukkan alamat anda\t: "))
noktp = str(input("masukkan no ktp anda\t: "))
notelepon = str(input("masukkan nomor telp anda\t: "))
jeniskendaraan = str(input("masukkan jenis kendaraan\t: "))
noplat = str(input("masukkan plat nomor\t: "))
lamasewa = int(input("berapa hari lamanya anda menyewa?\t "))
biayasewa = int(input("masukkan biaya sewa\t: "))




class sewakendaraan():
    def __init__(self, lamasewa, biayasewa):
        self.lamasewa = lamasewa
        self.biayasewa = biayasewa

    def TotalSewa(self):
        return self.lamasewa * self.biayasewa

    def PotonganHarga(self):
        if self.lamasewa >= 7:
            tl = self.TotalSewa() * 0.5
        elif self.lamasewa >= 5 and self.lamasewa < 7:
            tl = self.TotalSewa() * 0.3
        elif self.lamasewa >= 3 and seld.lamasewa <5:
            tl = self.TotalSewa() * 0.2
        else:
            tl = 0
        return tl

    def PPN(self):
        return self.TotalSewa() * 0.2

    def HarusBayar(self):
        return self.TotalSewa() - self.PotonganHarga() + self.PPN()

s = sewakendaraan(lamasewa, biayasewa)
prnt = str(f"{s.HarusBayar():,}")
print(prnt, " adalah grand total pembayaran anda")