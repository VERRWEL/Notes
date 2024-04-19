nilai_mhs = []

def Sort(arr, key):
  for index in range(len(arr)-1):
    smallestIndex = index
    for minIndex in range(index+1, len(arr)):
      if (arr[minIndex][key] < arr[smallestIndex][key]):
        smallestIndex = minIndex
    temp               = arr[index]
    arr[index]         = arr[smallestIndex]
    arr[smallestIndex] = temp

def Search(data, cari, key):
  hasil = []
  for i in range(len(data)):
    if (data[i][key] > cari):
      break
    else:
      if (data[i][key] == cari):
        hasil.append(i)

  if (len(hasil) > 0):
    print(f"Grade {cari} ditemukan:")
    for i in range(len(hasil)):
      print(f"<< Hasil Ke-{i+1} >>")
      for keys, values in data[hasil[i]].items():
        if (len(keys) < 10):
          print(f"{keys}\t\t: {values}")
        else:
          print(f"{keys}\t: {values}")
      print()
  else:
    print(f"Grade {cari} tidak ditemukan")

while True:
  data = {}
  data["Mata Kuliah"] = input("Masukkan Mata Kuliah\t: ")
  data["SKS"]         = int(input("Masukkan Jumlah SKS\t: "))
  data["Nilai Akhir"] = int(input("Masukkan Nilai Akhir\t: "))

  if (80 <= data["Nilai Akhir"] <= 100):
    data["Grade"] = "A"
  elif (60 <= data["Nilai Akhir"] < 80):
    data["Grade"] = "B"
  elif (data["Nilai Akhir"] < 60):
    data["Grade"] = "C"
  print("Grade\t\t\t:", data["Grade"])

  if (data["Grade"] == "A"):
    data["Bobot"] = 4
  if (data["Grade"] == "B"):
    data["Bobot"] = 3
  if (data["Grade"] == "C"):
    data["Bobot"] = 2
  print("Bobot\t\t\t:", data["Bobot"])

  data["Sub Total Bobot"] = data["SKS"] * data["Bobot"]
  print("Sub Total Bobot\t\t:", data["Sub Total Bobot"])

  nilai_mhs.append(data)

  print()
  konfirmasi = input("Masukkan Lagi (Y/N)? ").upper()
  print()
  if (konfirmasi == "N"):
    break

Sort(nilai_mhs, "Grade")

cari_data = input("Cari Grade: ")

print()
Search(nilai_mhs, cari_data, "Grade")