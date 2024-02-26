# Latihan soal struktur data
"""
membuat program yang dapat menyimpan dan menampilkan judul, nama pengarang, dan tahun terbit sebuah atau banyak
buku sekaligus. menggunakan class bernama book() dengan methods berupa detail() yang bertugas untuk menerima dan 
menyimpan data judul buku, pengarang buku, dan tahun terbit buku. method addbook() yang bertugas untuk meenambahkan
detail buku selama user masih ingin menambahkan buku. dan method terakhir yang bernama display() yang bertugas
untuk menampilkan data detail buku dengan rapih
"""

class book:
    
    def detail(self):
        self.title = input("judul buku: ")
        self.name = input("pengarang buku: ")
        self.year = int(input("tahun terbit: "))
    
    def addbook(self):
        n = int(input("jumblah buku yang diinput: "))
        self.collection = []
        for i in range(n):
            print()
            self.book = book()
            self.book.detail()
            self.collection.append(self.book)
        
    def display(self):
        for book in self.collection:
            print("judul", "pengarang", "tahun terbit", sep = '\t|', end='\n|')
            print(book.title, book.name, book.year, sep='\t|', end='\n|')

b1 = book()
b1.addbook()
b1.display()
