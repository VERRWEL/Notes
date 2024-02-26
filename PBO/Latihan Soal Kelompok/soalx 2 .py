import math

class Diskriminan:
    def _init_(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def hd(self):
        return self.B ** 2 - 4 * self.A * self.C

    def akarReal(self):
        d = self.hd()
        x1 = (-self.B + math.sqrt(d)) / (2 * self.A)
        x2 = (-self.B - math.sqrt(d)) / (2 * self.A)
        print("Akar Real")
        print("Nilai X1\t= ",x1)
        print("Nilai X2\t= ",x2)

    def akarKembar(self):
        d = self.hd()
        x1 = -self.B / (2 * self.A)
        x2 = x1
        print("Akar Kembar")
        print("Nilai X1\t= ",x1)
        print("Nilai X2\t= ",x2)

    def akarKompleks(self):
        r = -self.B / (2 * self.A)
        #bagian imajiner
        i = math.sqrt(math.fabs(self.hd())) / (2 * self.A)

        print("Nilai X1\t= ",str(r)+ "+" + str(i) + "i")
        print("Nilai X2\t= ",str(r)+ "+" + str(i) + "i")


#input nilai A B C
A = float(input("Masukan Nilai A\t = "))
B = float(input("Masukan Nilai B\t = "))
C = float(input("Masukan Nilai C\t = "))

disk = Diskriminan(A, B, C)

d = disk.hd()

if d>0:
    disk.akarReal()
    
elif d == 0:
    disk.akarKembar()

else:
    disk.akarKompleks()
