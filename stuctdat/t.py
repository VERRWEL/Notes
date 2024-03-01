"""Buatlah sebuah class bernama Restaurant yang memiliki atribut nama restoran, daftar menu
beserta harga, dan rating. Class ini harus memiliki method untuk menambahkan menu baru
beserta harganya, menghapus menu dari daftar, dan menampilkan daftar menu beserta harga
dan ratingnya. Program menggunakan loop while untuk menampilkan menu kepada pengguna
dan mengambil inputnya. Penggunaan match-case / if -elif-else digunakan untuk memilih
operasi yang sesuai dengan input pengguna. Menu program terdiri dari menambah menu baru,
menampilkan daftar menu, menghapus daftar menu."""

class Restaurant:
    def __init__(self,menu):
        self.menu = menu

    def tampil(self):
        for key, value in menu.items():
            print(f"{key} : Rp {value:,}")

    def tambah(self):
        pass

    def hapus(self):
        pass

    def action(self):
        print("1. tampil menu")
        print("2. tambah menu")
        print("3. hapus menu")
        act = str(input("silahkan pilih 1-3 : "))
        while True:
            if act == "1":
                r.tampil()
                break
            elif act == "2":
                r.tambah()
                break
            elif act == "3":
                r.hapus()
                break
            else:
                print("pilihan tidak tersedia")
                act = str(input("silahkan pilih 1-3 : "))


menu = {
    "nasi uduk" : 5000,
    "tempe goreng" : 3000,
    "ayam bakar" : 15000
}

r = Restaurant(menu)
r.action