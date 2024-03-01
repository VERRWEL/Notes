"""latihan
1.Buatkan sebuah kelas Gudang yang memiliki atribut barnag untuk menyimpan inventaris barang
dengan jumlahnya. Terdapat method untuk menambahkan item ke inventaris, menghapus item
dari inventaris, dan menampilkan semua barang yang ada di inventaris. Program menggunakan
loop while untuk menampilkan menu kepada pengguna dan mengambil inputnya. Penggunaan
match-case / if -elif-else digunakan untuk memilih operasi yang sesuai dengan input pengguna.
"""

barang = {
    "muffler" : 3,
    "2JZe" : 1,
    "head gasket" : 4,
    "engine block" : 6,
    "ECU" : 10
}


class Gudzz:
    def __init__(self, barang):
        self.barang = barang
        if len(self.barang) == 1:
            self.disp = list(self.barang)[0]
        if len(self.barang) >= 2:
            self.disp = list(self.barang)[-1]

    def tambah_barang(self):
        self.tambah = str(input("masukkan nama barang : "))
        

        if self.tambah in self.barang:
            self.jumblah = int(input(f"berapa banyak {self.tambah} yang ingin ditambahkan : "))
            self.barang[self.tambah] = self.barang[self.tambah] + self.jumblah
        
        if self.tambah not in self.barang:
            self.jumblah = int(input(f"berapa jumblah barang {self.tambah} : "))
            self.barang[self.tambah] = self.jumblah

        for key, value in self.barang.items():
            print(key, ":", value)

        print(f"\n{self.jumblah} {self.tambah} berhasil ditambahkan")
        again = str(input("masih mau menambahkan barang? (y/n) "))
        if again == "y":
            x.tambah_barang()
        elif again == "n":
            x.opsi()
        else:
            print("pilihan anda \"", again, "\" aneh")

    def hapus_barang(self):
        if len(self.barang) == 0:
            print("\nisi gudang sudah kosong dan tidak ada lagi yang bisa dihapus")
            x.opsi()
        
        hapus = int(input(f"\n1. hapus semua barang \n2. edit barang terakhir ({self.disp}) \n3. pilih manual \n4. Batal\nsilahkan pilih opsi 1-4 dari atas  : "))
        if hapus == 1:
            self.barang.clear()
            print()
            x.opsi()
        if hapus == 2:
            hapus2 = int(input("\n1. hapus semua \n2. edit manual \n1/2? "))
            if hapus2 == 1: 
                del self.barang[self.disp]
                x.opsi()
            elif hapus2 == 2:
                hasil_hapus2 = int(input(f"berapa ({self.disp}) yang ingin dikurangi, sekarang ada {self.barang[self.disp]} : "))
                hasil_hapus3 = self.barang[self.disp] - hasil_hapus2
                self.barang[self.disp] = hasil_hapus3
                print(f"berhasil mengurangi {self.disp} dari {self.barang[self.disp] + hasil_hapus2} ke {self.barang[self.disp]} ")
                x.opsi()

        if hapus == 3:
            for key, value in self.barang.items():
                print(key, ":", value)
            
            manual = str(input("barang mana yang mau di edit? "))
            if manual in self.barang:
                edit = int(input(f"berapa banyak unit {manual} yang ingin dikurangi, sekarang ada {self.barang[manual]} : "))
                self.barang[manual] = self.barang[manual] - edit
                print(f"{manual} berhasil dikurangi menjadi {self.barang[manual]}")
            else:
                print("barang yang dicari tidak ditemukan \nNote: nama barang harus case sensitive")
            x.opsi()
        
        if hapus == 4:
            print()
            print("kembalikan ke menu pilihan")
            x.opsi()

        for i in self.barang.keys():
            if self.barang[i] < 1:
                del self.barang[i]

    def lihat_barang(self):
        print()
        if len(self.barang) == 0:
            print("\nisi gudang sudah kosong dan tidak ada lagi yang bisa dihapus")
        for key, value in self.barang.items():
            print(key, ":", value)
        print()
        x.opsi()
        
    def opsi(self):
        opp = int(input("1. lihat barang \n2. tambah barang \n3. hapus barang \n4. keluar \npilih opsi 1-4 diatas ini : "))
        while True:
            if opp == 1:
                x.lihat_barang()
                break
            elif opp == 2:
                x.tambah_barang()
                break
            elif opp == 3:
                x.hapus_barang()
                break
            elif opp == 4:
                print("otw exit program")
                break
            else:
                print()
                print(f"error! pilihan anda ({opp}) tidak tersedia")
                break

x=Gudzz(barang)
x.opsi()
