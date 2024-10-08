from datetime import datetime, timedelta

# Daftar Kacamata
kacamata_kategori = {
    "Fashion": [
        {"kode": "K001", "nama": "Kacamata Hitam", "harga": 150000},
        {"kode": "K005", "nama": "Kacamata Retro", "harga": 180000}
    ],
    "Fungsional": [
        {"kode": "K002", "nama": "Kacamata Baca", "harga": 100000},
        {"kode": "K004", "nama": "Kacamata Anti Radiasi", "harga": 250000}
    ],
    "Olahraga": [
        {"kode": "K003", "nama": "Kacamata Renang", "harga": 200000},
        {"kode": "K006", "nama": "Kacamata Sepeda", "harga": 220000}
    ]
}

# nyimpen pesanan
stack_pesanan = []

#menampilkan kategori
def tampilkan_semua_kategori():
    print("Kategori Kacamata yang Tersedia:")
    for kategori in kacamata_kategori.keys():
        print(f"- {kategori}")

def tampilkan_kacamata_berdasarkan_kategori(kategori):
    if kategori in kacamata_kategori:
        print(f"Daftar Kacamata Kategori: {kategori}")
        for kacamata in kacamata_kategori[kategori]:
            print(f"Kode: {kacamata['kode']}, Nama: {kacamata['nama']}, Harga: {kacamata['harga']}")
        return 1
    else:
        print("Kategori tidak ditemukan.")
        return 0

# mencari kacamata (berdasarkan kode) 
def cari_kacamata(kode):
    for kategori in kacamata_kategori.values():
        for kacamata in kategori:
            if kacamata["kode"] == kode:
                return kacamata
    return None

# Memesan kacamata
def pesan_kacamata():
    nama_pemesan = input("Masukkan nama pemesan: ")
    tampilkan_semua_kategori()
    kategori_pilihan = input("Masukkan kategori kacamata yang diinginkan: ")
    #tampilkan_kacamata_berdasarkan_kategori(kategori_pilihan)
    if tampilkan_kacamata_berdasarkan_kategori(kategori_pilihan) == 0:
        pesan_kacamata()
        return
    kode_barang = input("Masukkan kode barang: ")
    kacamata = cari_kacamata(kode_barang)
    if kacamata:
        quantity = int(input("Masukkan jumlah pemesanan: "))
        tanggal_pemesanan = datetime.now()
        perkiraan_dikirim = tanggal_pemesanan + timedelta(days=2)
        perkiraan_sampai = perkiraan_dikirim + timedelta(days=3)
        
        total_harga = kacamata["harga"] * quantity
        
        # data yang sudah disimpan kedalam stack
        pesanan = {
            "nama_pemesan": nama_pemesan,
            "barang": kacamata["nama"],
            "kode_barang": kode_barang,
            "quantity": quantity,
            "tanggal_pemesanan": tanggal_pemesanan,
            "perkiraan_dikirim": perkiraan_dikirim,
            "perkiraan_sampai": perkiraan_sampai,
            "total_harga": total_harga
        }
        
        stack_pesanan.append(pesanan)
        print("\nPesanan telah ditambahkan ke dalam stack.")
    else:
        print("Kode barang tidak ditemukan.")

# melihat semua pesanan terbaru 
def lihat_semua_pesanan():
    if stack_pesanan:
        print("\nDaftar Semua Pesanan:")
        # Menampilkan pesanan dari yang baru sampai yang lama
        for nomor_pesanan, pesanan in enumerate(reversed(stack_pesanan), start=1):
            print(f"\nPesanan {nomor_pesanan}:")
            print(f"Nama Pemesan: {pesanan['nama_pemesan']}")
            print(f"Barang: {pesanan['barang']} ({pesanan['kode_barang']})")
            print(f"Jumlah: {pesanan['quantity']}")
            print(f"Tanggal Pemesanan: {pesanan['tanggal_pemesanan'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Perkiraan Dikirim: {pesanan['perkiraan_dikirim'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Perkiraan Sampai: {pesanan['perkiraan_sampai'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Total Harga: {pesanan['total_harga']}")
    else:
        print("Tidak ada pesanan dalam stack.")

# Main program untuk interaksi dengan pengguna
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Pesan Kacamata")
        print("2. Lihat Semua Pesanan")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            pesan_kacamata()
        elif pilihan == "2":
            lihat_semua_pesanan()
        elif pilihan == "3":
            print("\nKeluar dari program. Berikut adalah semua pesanan yang tersimpan:")
            lihat_semua_pesanan()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")