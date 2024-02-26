"""
Buat program untuk
menghitung grade nilai. Bobot
uts adalah 30%, tugas 20%, uas
50%. Untuk totalnilai = uts+tugas+uas. 
Grade: 
jika totalnilai >= 80 maka "A", 
jika totalnilai >= 60 maka "B", 
jika totalnilai >= 40 maka "C", 
jika totalnilai >= 20 maka "D", 
jika totalnilai <= 19 maka "E".
"""

uts = float(input("masukkan nilai uts: "))
uas = float(input("masukkan nilai uas: "))
tm = float(input("masukkan nilai TM: "))

class nilai():
    def __init__(self,uts,uas,tm):
        self.uts =  uts
        self.uas = uas
        self.tm = tm

    def outUTS(self):
        hsts = self.uts * 0.3
        hsas = self.uas * 0.4
        hstm = self.uas * 0.3
        return hsts + hsas + hstm
    
    def output(self):
        global s
        if self.outUTS() >= 80:
            s = str("A")
        elif self.outUTS() >= 73 and self.outUTS() <= 79.99:
            s = str("B+")
        elif self.outUTS() >= 66 and self.outUTS() <= 72.99:
            s = str ("B")
        elif self.outUTS() >= 58 and self.outUTS() <= 65.99:
            s = str("C+")
        elif self.outUTS() >= 51 and self.outUTS() <= 57.99:
            s = str("C")
        elif self.outUTS() >= 41 and self.outUTS() <= 50.99:
            s = str("D")
        else:
            s = str("E")
        return s
    

n = nilai(uts, uas, tm)
print(n.output(), "karena nilai anda : ", n.outUTS())
