# SOAL 1 ALGORITMA LANJUT

students = [
            {"NAMA": "richard", "ALPRO": "90", "DISKRIT": "91"},
            {"NAMA": "jonathan" , "ALPRO": "90" , "DISKRIT": "81"},
            {"NAMA": "yehezkiel" , "ALPRO": "95" , "DISKRIT": "75"},
            ]

def ascending_sort(data,find):
  length = len(data)

  for i in range(length - 1):
    for j in range(0, length - i - 1):
      if data[j][find] > data[j+1][find]:
        data[j],data[j + 1] = data[j + 1],data[j]
  return data

def search(cari):
  found = False
  for student in students:
      if student["NAMA"] == cari:
          print(f"data {cari} ditemukan: {student}")
          found = True
          break  
  if not found:
    print(f"Student with name {cari} not found")

x= ascending_sort(students, 'DISKRIT')
print("pengurutan nilai DISKRIT : ")
for i in x:
  print(i)

carinama = str(input("\nmasukan nama yang ingin dicari : ")) 
search(carinama)



