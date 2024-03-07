#membuat class Node untuk menyimpan nilai dan alamat dari elemen berikutnnya
class Node:
    def __init__(self):
        self.data = input("Data: ")
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add1st(self):           #Fungsi menambahkan elemen di linkedlist
        simpul = Node()         #var simpul = fungsi Node() yang membuattnya memiliki constructor dari class Node()
        if self.head is None:
            self.head = simpul
            return
        simpul.next = self.head
        self.head = simpul
    
    def addend(self):
        simpul = Node()
        #cek apakah list kosong
        if self.head is None:
            self.head = simpul
            return
        #jika list tidak kosong
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = simpul

    def print(self):            #fungsi unruk menampilkan isi dari linked list
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print('Name\n')

#mengakses class single linked list dan menambahkan elemen ke dalam list
sll = LinkedList()
sll.add1st()
sll.add1st()
sll.addend()
sll.print()
