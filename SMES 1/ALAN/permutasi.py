def permutasi_dac(string):
  """
  Menghasilkan semua kemungkinan permutasi string dengan divide and conquer.

  Args:
    string: String yang ingin di permutasi.

  Returns:
    List berisi semua kemungkinan permutasi string.
  """
  if len(string) == 0:
    return [""]

  permutasi = []
  for i in range(len(string)):
    char = string[i]
    sisa_string = string[:i] + string[i+1:]

    # Divide and conquer untuk menghasilkan permutasi sisa string
    permutasi_sub = permutasi_dac(sisa_string)

    # Menggabungkan karakter dengan setiap permutasi sub-string
    for perm in permutasi_sub:
      if char not in perm:
        permutasi.append(perm + char)
      permutasi.append(char + perm)

  return permutasi

string = "abc"
permutasi = permutasi_dac(string)
print(permutasi)