class Book:
  def __init__(self, title, author, publication_year, publisher, isbn):
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
      print(f"author: {self.author}")
      print(f"publication year: {self.publication_year}")
      print(f"publisher: {self.publisher}")
      print(f"ISBN: {self.isbn}")
      print(f"Available: {self.available}\n")  

class Library:
  def __init__(self, books=None):
    if books is Noone:
      self.books = []
    else:
      self.books = books

  def add_book(self,book):
    self.books.append(book)

  def remove_book(self, book):
    for book in self.books:
      book.display_book()

book1 = Book("Harry Potter", "J.K Rowling", 2000, "Cukurukuk", "32230374830")
library = Library()
library.add_book(book1)
    
