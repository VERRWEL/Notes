#membuat class Node untuk menyimpan nilai dan alamat dari elemen berikutnnya
class Node:
    def __init__(self):
        self.data = input("Data: ")
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add1st(self):           #Fungsi menambahkan elemen pertama di linkedlist
        simpul = Node()         #var simpul = fungsi Node() yang membuattnya memiliki constructor dari class Node()
        if self.head is None:
            self.head = simpul
            return
        simpul.next = self.head
        self.head = simpul

    def addmid(self):
        posisi = int(input("Input posisi elemen: "))
        simpul = Node()
        #Jika list kosong maka tidak bisa menambahkan elemen di posisi tersebut
        if self.head is None:
            print("List masih kosong. tdak bisa menambahkan elemen di posisi tersebut.")
            return
        #Jika list tidak kosong maka tambahkan elemen di posisi yang diinginkan
        x = 0 #var untuk menyimpan posisi elemen dalam list
        temp = self.head
        while(temp.next != None and x+1 != posisi):
            temp = temp.next
            x = x + 1
            if x + 1 == posisi:
                simpul.next = temp.next
                temp.next = simpul

    def addend(self):           #fungsi menambahkan elemen di akhir list dalam linked list
        simpul = Node()
        #cek apakah list kosong maka tambahkan elemen dalam list
        if self.head is None:
            self.head = simpul
            return
        #jika list tidak kosong maka posisikan elemen yang baru ditambahkan ke posisi akhir di linked list
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = simpul

    def showlist(self):            #fungsi unruk menampilkan isi dari linked list
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print('Name\n')

#mengakses class single linked list dan menambahkan elemen ke dalam list
sll = LinkedList()
print("add1st\naddmid\naddend")
pilih = str(input("1/2/3? "))
while True:
    if pilih == "1":
        sll.add1st()
        print("add1st\naddmid\naddend")
        pilih = str(input("1/2/3? "))
    elif pilih == "2":
        sll.addmid()
        print("add1st\naddmid\naddend")
        pilih = str(input("1/2/3? "))
    elif pilih == "3":
        sll.addend()
        print("add1st\naddmid\naddend")
        pilih = str(input("1/2/3? "))
    else:
        print("mengeluarkan program...")
        bbbb
        
