def pembalik_angka():
    ### PEMBALIK ANGKA
    angka = int(input("masukan angka: "))
    reverse = 0
    while(angka > 0):
        reminder = angka % 10
        reverse = (reverse * 10) + reminder
        angka = angka//10

    print("data setelah dibalik : %d" %reverse)

def coklat():
    ### COKLAAT
    import math

    def maxcoklat(uang,harga,wrap):
        coklat = uang/harga
        return math.floor(coklat + hitungextra(coklat,wrap))

    def hitungextra(coklat, wrap):
        if(coklat<wrap):
            return 0
        extra = coklat//wrap
        return extra + hitungextra(extra + coklat % wrap, wrap)

    a = int(input("harga coklat : Rp "))
    b = int(input("bekas coklat untuk mendapatkan 1 coklat: "))
    c = int(input("uang yang ada : Rp "))

    result = maxcoklat(c, a, b)
    print("maksimal coklat yang bisa didapatkan adalah {} bungkus".format(result))
    print()

