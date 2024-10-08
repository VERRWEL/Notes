hewan_kecil = {}
hewan_sedang = {}
hewan_besar = {}
hewan = [hewan_kecil, hewan_sedang, hewan_besar]

#menginput batas kapasitas masing-masing hewan:
max_hewan_kecil = int(input("berapa maximal sangkar hewan kecil? "))
max_hewan_sedang = int(input("berapa maximal sangkar hewan sedang? "))
max_hewan_besar = int(input("berapa maximal sangkar hewan besar? "))

#menginput hewan yang ingin dimasukkan berdasarkan ukurannya:
def input_hewan(max_hewan_kecil, max_hewan_sedang, max_hewan_besar):
    print("\nberikut kategori ukuran hewan: \n1. kecil \n2. sedang \n3. besar")
    ukuran_hewan = str(input("apa ukuran hewan yang ingin dimasukkan? "))
    
    if (ukuran_hewan == "kecil") or (ukuran_hewan == "1"):
        print("batas kapasitas hewan kecil saat ini: ", max_hewan_kecil)
        nama_hewan_masuk = str(input("apa nama hewan yang ingin dimasukkan? "))
        jumlah_hewan_masuk = int(input(f"berapa banyak {nama_hewan_masuk} yang ingin dimasukkan? "))
        if jumlah_hewan_masuk <= max_hewan_kecil:
            hewan_kecil[nama_hewan_masuk] = jumlah_hewan_masuk
            max_hewan_kecil = max_hewan_kecil - jumlah_hewan_masuk
            print(f"berhasil menambahkan {jumlah_hewan_masuk} {nama_hewan_masuk} kedalam sangkar hewan kecil")
        else:
            print("gagal menambahkan karena kapasitas sudah penuh")
    
    elif (ukuran_hewan == "sedang") or (ukuran_hewan == "2"):
        print("batas kapasitas hewan sedang saat ini: ", max_hewan_sedang)
        nama_hewan_masuk = str(input("apa nama hewan yang ingin dimasukkan? "))
        jumlah_hewan_masuk = int(input(f"berapa banyak {nama_hewan_masuk} yang ingin dimasukkan? "))
        if jumlah_hewan_masuk <= max_hewan_sedang:
            hewan_sedang[nama_hewan_masuk] = jumlah_hewan_masuk
            max_hewan_sedang = max_hewan_sedang - jumlah_hewan_masuk
            print(f"berhasil menambahkan {jumlah_hewan_masuk} {nama_hewan_masuk} kedalam sangkar hewan sedang")
        else:
            print("gagal menambahkan karena kapasitas sudah penuh")
    
    elif (ukuran_hewan == "besar") or (ukuran_hewan == "3"):
        print("batas kapasitas hewan besar saat ini: ", max_hewan_besar)
        nama_hewan_masuk = str(input("apa nama hewan yang ingin dimasukkan? "))
        jumlah_hewan_masuk = int(input(f"berapa banyak {nama_hewan_masuk} yang ingin dimasukkan? "))
        if jumlah_hewan_masuk <= max_hewan_besar:
            hewan_besar[nama_hewan_masuk] = jumlah_hewan_masuk
            max_hewan_besar = max_hewan_besar - jumlah_hewan_masuk
            print(f"berhasil menambahkan {jumlah_hewan_masuk} {nama_hewan_masuk} kedalam sangkar hewan besar")
        else:
            print("gagal menambahkan karena kapasitas sudah penuh")
    else:
        print(f"\nukuran {ukuran_hewan} tidak ada")
        print("silahkan coba lagi")
        input_hewan(max_hewan_kecil, max_hewan_sedang, max_hewan_besar)
        return max_hewan_kecil, max_hewan_sedang, max_hewan_besar
    
    inpt_again = str(input("\napakah ingin menambahkan hewan lagi? (ya/tidak) "))
    if inpt_again == "ya":
        input_hewan(max_hewan_kecil, max_hewan_sedang, max_hewan_besar)
    elif inpt_again == "tidak":
        print("terimakasih")
    else:
        print("terimakasih")

    return max_hewan_kecil, max_hewan_sedang, max_hewan_besar

def display_hewan(hewan_kecil, hewan_sedang, hewan_besar):
    print()
    print("\nsangkar hewan kecil :")
    if len(hewan_kecil) == 0:
        print("sangkar hewan kecil kosong")
    else:
        for hewan in hewan_kecil:
            print(f"{hewan} : {hewan_kecil[hewan]}")

    print("\nsangkar hewan sedang :")
    if len(hewan_sedang) == 0:
        print("sangkar hewan sedang kosong")
    else:
        for hewan in hewan_sedang:
            print(f"{hewan} : {hewan_sedang[hewan]}")

    print("\nsangkar hewan besar :")
    if len(hewan_besar) == 0:
        print("sangkar hewan besar kosong")
    else:
        for hewan in hewan_besar:
            print(f"{hewan} : {hewan_besar[hewan]}")

def check_kapasitas(max_hewan_kecil, max_hewan_sedang, max_hewan_besar):
    print("sangkar hewan kecil : ", max_hewan_kecil)
    print("sangkar hewan sedang : ", max_hewan_sedang)
    print("sangkar hewan besar : ", max_hewan_besar)
    
max_hewan_kecil, max_hewan_sedang, max_hewan_besar = input_hewan(max_hewan_kecil, max_hewan_sedang, max_hewan_besar)
while True:
    print("\n1. input hewan \n2. display hewan \n3. mengecek kapasitas semua sangkar \n4. exit")
    opsi = str(input("apa yang ingin anda lakukan? "))

    if (opsi == "1") or (opsi == "input hewan"):
        input_hewan(max_hewan_kecil, max_hewan_sedang, max_hewan_besar)

    elif (opsi == "2") or (opsi == "display hewan"):
        display_hewan(hewan_kecil, hewan_sedang, hewan_besar)

    elif (opsi == "3") or (opsi == "mengecek kapasitas semua sangkar"):
        check_kapasitas(max_hewan_kecil, max_hewan_sedang, max_hewan_besar)

    elif (opsi == "4") or (opsi == "exit"):
        print("terimakasih")
        break
