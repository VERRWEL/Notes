# Codingan Gus
# membuat program berbasis PBO dengan minimal 8 parameter dan minimal 4 method, Temanya bebas
class Mobil:
    def __init__(self, merek, model, tahun, warna,kecepatan = 0, mesin_mati = True, bahan_bakar = "bensin", status_kunci="mati"):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.warna = warna
        self.kecepatan = kecepatan
        self.mesin_mati = mesin_mati
        self.bahan_bakar = bahan_bakar
        self.status_kunci = status_kunci

    def nyalakan_mesin(self):
        if not self.mesin_mati:
            print("Mesin sudah menyala")
        else:
            self.mesin_mati = False
            print("Mesin berhasil dinyalakan")

    def matikan_mesin(self):
        if self.mesin_mati:
            print("Mesin sudah mati")
        else:
            self.mesin_mati = False
            print("Mesin berhasil dimatikan")
    
    def kunci_mobil(self):
        if self.status_kunci == "mati":
            self.status_kunci = "hidup"
            print("Kunci mobil di hidupkan")
        else:
            self.status_kunci = "mati"
            print("Kunci mobil dimatikan")

    def tambah_kecepatan(self, tambahan_kecepatan):
        if self.mesin_mati:
            print("Mesin mati, tidak bisa tambah kecepatan")
        else:
            self.kecepatan += tambahan_kecepatan
            print(f"Kecepatan berhasil di tambahkan. Kecepatan sekarang:{self.kecepatan} km/jam")

mobil_saya = Mobil(merek="Toyota", model="Camry", tahun=2022,warna="Hitam")
mobil_saya.nyalakan_mesin()
mobil_saya.kunci_mobil()
mobil_saya.tambah_kecepatan(20)
mobil_saya.matikan_mesin