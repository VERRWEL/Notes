class Book:
  def __init__(self, title, author, publication year, publisher, isbn):
    self.title = title
    self.autor = author
    self.publication_year = publication_year
    self.publisher = publisher
    self.isbn = isbn
    self.available = True
  def borrow_book(self):
    if self.available:
      self.available = False
      print(f"{self.title} sudah dipinjam")
    else:
      print(f"{self.title} buku tidak ada")

  def return_book(self):
    if not self.available:
      self.available = True
      print(f"{self.title} sudah dikembalikan")
    else:
      print(f"{self.title} sudah ada")
    def displai_book(self):
      print(f"title: {self.title}")
      
