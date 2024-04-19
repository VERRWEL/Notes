import math

A=float(input("Masukkan nilai pertama(A): "))
B=float(input("Masukkan nilai pertama(B): "))
C=float(input("Masukkan nilai pertama(C): "))

def NilaiDiskriminan(A,B,C):
    disc = B**2 - 4 * A * C
    if disc > 0:
        x1 = (-B + math.sqrt(disc)) / (2 * A)
        x2 = (-B - math.sqrt(disc)) / (2 * A)

        print("Akar Real")
        print("Nilai variabel x1 = ", x1)
        print("Nilai variabel x2 = ", x2)
    
    elif disc == 0:
        x1 = -B / (2 * A)
        x2 = x1
        print("Akar Kembar")
        print("Nilai variabel x1 = ", x1)
        print("Nilai variabel x2 = ", x2)
    
    else:
        ril = -b / (2 * A)
        imagine = math.sqrt(abs(disc)) / (2 * A)
        print("akar kompleks")
        print("Nilai variabel x1 = ", ril, " + ", imagine, " i")
        print("Nilai x2 = ", ril, " - ", imagine, " i")

NilaiDiskriminan(A,B,C)
