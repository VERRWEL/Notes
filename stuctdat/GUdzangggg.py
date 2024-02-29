"""latihan
1.Buatkan sebuah kelas Gudang yang memiliki atribut barnag untuk menyimpan inventaris barang
dengan jumlahnya. Terdapat method untuk menambahkan item ke inventaris, menghapus item
dari inventaris, dan menampilkan semua barang yang ada di inventaris. Program menggunakan
loop while untuk menampilkan menu kepada pengguna dan mengambil inputnya. Penggunaan
match-case / if -elif-else digunakan untuk memilih operasi yang sesuai dengan input pengguna.

2. Buatlah sebuah class bernama Restaurant yang memiliki atribut nama restoran, daftar menu
beserta harga, dan rating. Class ini harus memiliki method untuk menambahkan menu baru
beserta harganya, menghapus menu dari daftar, dan menampilkan daftar menu beserta harga
dan ratingnya. Program menggunakan loop while untuk menampilkan menu kepada pengguna
dan mengambil inputnya. Penggunaan match-case / if -elif-else digunakan untuk memilih
operasi yang sesuai dengan input pengguna. Menu program terdiri dari menambah menu baru,
menampilkan daftar menu, menghapus daftar menu."""

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

    def tambah_barang(self):
        self.tambah = str(input("masukkan nama barang : "))
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
        elif len(self.barang) == 1:
            disp = list(self.barang)[0]
        else:
            disp = list(self.barang)[-1]

        
        hapus = int(input(f"\n1. hapus semua barang \n2. edit barang terakhir ({disp}) \n3. pilih manual \n4. Batal\nsilahkan pilih opsi 1-4 dari atas  : "))
        if hapus == 1:
            self.barang.clear()
        if hapus == 2:
            hapus2 = int(input("\n1. hapus semua \n2. edit manual \n1/2? "))
            if hapus2 == 1: 
                del self.barang[disp]
            elif hapus2 == 2:
                hasil_hapus2 = int(input(f"berapa ({disp}) yang ingin dikurangi, sekarang ada {self.barang[disp]} : "))
                hasil_hapus3 = self.barang[disp] - hasil_hapus2
                self.barang[disp] = hasil_hapus3
                print(f"berhasil mengurangi {disp} dari {self.barang[disp] + hasil_hapus2} ke {self.barang[disp]} ")
                if self.barang[disp] == 0:
                    del self.barang[disp]

        if hapus == 3:
            for key, value in self.barang.items():
                print(key, ":", value)
            
            manual = str(input("barang mana yang mau di edit? "))
            try:
                edit = str(input(f"berapa banyak unit {manual} yang ingin dikurangi : "))
                self.barang[manual] = self.barang[manual] - edit
                print("berhasil mengurangi ")
            except:
                print("barang yang dicari tidak ditemukan \nNote: nama barang harus case sensitive")
            x.opsi()
            
        if hapus == 4:
            print()
            x.opsi()

    def lihat_barang(self):
        print()
        for key, value in self.barang.items():
            print(key, ":", value)
        print()
        x.opsi()
        
    def opsi(self):
        opp = int(input("1. lihat barang \n2. tambah barang \n3. hapus barang \n4. keluar \npilih opsi 1-4 diatas ini : "))
        while opp != 4:
            if opp == 1:
                x.lihat_barang()
            elif opp == 2:
                x.tambah_barang()
            elif opp == 3:
                x.hapus_barang()
            else:
                print("error")

x=Gudzz(barang)
x.opsi()