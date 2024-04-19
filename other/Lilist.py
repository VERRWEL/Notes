

mhs = []

while True:
  data = {}
  data["nama"] = input("Masukkan Nama\t: ")
  data["nim"]  = input("Masukkan NIM\t: ")
  data["ipk"]  = float(input("Masukkan IPK\t: "))

  mhs.append(data)

  print()
  konfirmasi = input("Masukkan Lagi (Y/N)? ").upper()
  print()
  if (konfirmasi == "N"):
    break

for i in range(len(mhs)):
  print("Nama :", mhs[i]["nama"], "\t| Alamat:", (mhs[i]["nama"]))
  print("NIM  :", mhs[i]["nim"] , "\t| Alamat:", (mhs[i]["ipk"]))
  print("IPK  :", mhs[i]["ipk"] , "\t| Alamat:", (mhs[i]["ipk"]))
  print()