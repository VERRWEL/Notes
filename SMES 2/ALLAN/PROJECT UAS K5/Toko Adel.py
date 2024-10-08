produk_toko = { # dictionary yang menyimpan produk-produk toko
    "roti" : 18000,
    "minuman dingin" : 10000,
    "minyak goreng" : 27000,
    "telur" : 3000,
    "shampoo" : 30000,
    "rokok" : 38000,
    "korek api" : 5000
} 

barang_belanjaan = {} # keranjang belanjaan pelanggan
def BeliBarang(): # method menambahkan barang
    print()
    print("barang yang tersedia : ")
    for barang in produk_toko: #loop untuk mengoutput produk-produk yang tersedia
        print(f"{barang : ^15} : {produk_toko[barang]}")

    tambah_barang = str(input("\nbarang apa yang mau di tambahkan (input \"x\" untuk selesai) : ")) # inputan untuk menambahkan barang ke keranjang
    
    if tambah_barang in produk_toko: # jika inputan(tambah_barang) tersedia dan ada di dictionary(produk_toko), maka tambahkan barang tersebut ke keranjang
        jumblah_barang = int(input(f"berapa jumblah {tambah_barang} yang ingin diambil : ")) # inputan untuk berapa jumblah barang barusan
        barang_belanjaan[tambah_barang] = jumblah_barang
        print(f"\n{tambah_barang} berhasil ditambahkan ke keranjang")
        BeliBarang() # panggil lagi method dirinya sendiri yaitu def BeliBarang untung mengulangi inputan
    elif tambah_barang == "x": # jika inputan(tambah_barang) adalah "x" maka method def BeliBarang akan berhenti
        print("selesai menambahkan barang belanjaan")
        return # memberhentikan method
    elif tambah_barang not in produk_toko: # jika inputan(tambah_barang) tidak tersedia dan tidak ada di dictionary(produk_toko), maka barang tidak ditambahkan dan inputan di ulang lagi
        print(f"\n\"{tambah_barang}\" tak tersedia dalam toko") 
        BeliBarang() # panggil lagi method dirinya sendiri yaitu def BeliBarang untung mengulangi inputan

def HitungTotal(tb): # method untuk menghotung total barang belanjaan
    for barang in barang_belanjaan:
        tb = tb + produk_toko[barang] * barang_belanjaan[barang]
    return tb
        
def HitunganAkhir(total):
    diskon_total = 0
    if (total >= 70000 and total <= 100000):
        diskon1 = total * 0.05   
        diskon_total = diskon_total + diskon1
        total = total - diskon1
    elif (total >= 100001 and total <= 180000):
        diskon2 = total * 0.06
        diskon_total = diskon_total + diskon2
        total = total - diskon2
    elif (total >= 180001 and total <= 250000):
        diskon3 = total * 0.09
        diskon_total = diskon_total + diskon3
        total = total - diskon3
    elif total > 200000:
        diskon4 = total * 0.11
        diskon_total = diskon_total + diskon4
        total = total - diskon4
    if len(barang_belanjaan) > 7:
        barang_termurah = min(barang_belanjaan.values())
        diskon_total = diskon_total + barang_termurah
        total = total - barang_termurah

    pajak = total * 0.10
    total = total + pajak

    return total, diskon_total, pajak

BeliBarang()
harga_total_barang = HitungTotal(0)

print("\nberikut isi barang belanjaan anda : ")
for barang in barang_belanjaan:
        print(f"{barang}")
print()

total_harga, total_diskon, total_pajak = HitunganAkhir(harga_total_barang)
print(total_harga)
pembayaran = int(input(f"Harga akhir adalah {total_harga} \n berapa uang yang anda ingin beri : "))
while pembayaran < total_harga:
    int(input("uang tidak cukup, mohon masukan nominal yang dapat diterima : "))
    pembayaran = int(input(f"Harga akhir adalah {total_harga} \n berapa uang yang anda ingin beri : "))

print("\nStruk Belanja: ")
print(f"{'Barang' : <15}{'Harga' : ^15}{'Jumlah' : ^15}{'Total Harga' : >15}")
print(f"{'------' : <15}{'-----' : ^15}{'------' : ^15}{'-----------' : >15}")
for barang in barang_belanjaan:
    print(f"{barang : <15}{produk_toko[barang] : ^15}{barang_belanjaan[barang] : ^15}{produk_toko[barang]*barang_belanjaan[barang] : >15}")
print("----------------------------")
print("Total Belanja =", int(harga_total_barang))
print("Diskon =", int(total_diskon))
print("Total Pajak =", total_pajak)
print("Total Pembayaran =", total_harga)
print("Uang Dibayar =", pembayaran)
print("Uang Kembalian =", pembayaran - total_harga)