class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def _init_(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.is_empty():
            removed = self.head
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return removed.data
        else:
            return None

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

class Flight:
    def _init_(self, flight_number, destination, capacity, price, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.available_seats = capacity
        self.price = price
        self.departure_time = departure_time
        self.total_sales = 0  # Total penjualan tiket

    def check_availability(self):
        return self.available_seats > 0

    def book_seat(self, num_seats):
        if self.available_seats >= num_seats:
            self.available_seats -= num_seats
            total_price = self.price * num_seats
            self.total_sales += total_price
            print(f"{num_seats} kursi yang dipesan untuk Penerbangan {self.flight_number} ke {self.destination}.")
            print(f"Total harga tiket untuk pesanan ini: {total_price}")
        else:
            print(f"Maaf, kursi yang tersedia tidak mencukupi.")
            print(f"Sisa kursi untuk Penerbangan {self.flight_number} ke {self.destination}: {self.available_seats}")
            while True:
                try_again = input("Apakah Anda ingin mencoba lagi? (ya/tidak): ")
                if try_again.lower() == "ya":
                    num_seats = int(input("\nMasukkan jumlah kursi: "))
                    self.book_seat(num_seats)
                    break
                elif try_again.lower() == "tidak":
                    return  # Kembali ke menu utama
                else:
                    print("Masukkan ya atau tidak.")

def display_schedule(flights):
    print("\nJadwal Tiket Pesawat:")
    for flight in flights:
        print(f"Penerbangan {flight.flight_number} ke {flight.destination} - Waktu keberangkatan: {flight.departure_time} - Kursi yang Tersedia: {flight.available_seats}")

def main():
    print("Selamat Datang di Bandara Internasional Soekarno-Hatta")
    passport_number = input("Masukkan nomor paspor Anda: ")
    nama_user = input("Masukkan nama Anda: ")

    print(f"\nTerima kasih, {nama_user} ({passport_number}), atas kunjungannya!")
    print("Berikut ini adalah Menu Pilihan Jadwal dan Pemesanan Tiket Pesawat")
    flights = [
        Flight("F001", "New York", 200, 500, "08:00"),
        Flight("F002", "London", 150, 700, "10:00"),
        Flight("F003", "Tokyo", 180, 800, "12:00"),
        Flight("F004", "Paris", 220, 600, "14:00"),
        Flight("F005", "Sydney", 180, 900, "16:00")
    ]

    booked_flights_info = []  # Menyimpan informasi penerbangan yang telah dipesan

    while True:
        print("\n--== MENU UTAMA ==--")
        print("1. Periksa Jadwal Penerbangan")
        print("2. Pesan Tiket")
        print("3. Tampilkan Pesanan Anda")
        print("4. Keluar")
        choice = input("Masukkan nomor Pilihan Anda: ")

        if choice == "1":
            display_schedule(flights)
        elif choice == "2":
            while True:
                flight_number = input("\nMasukkan nomor kode penerbangan: ")
                for flight in flights:
                    if flight.flight_number == flight_number:
                        if flight.check_availability():
                            num_seats = int(input("Masukkan jumlah kursi: "))
                            flight.book_seat(num_seats)
                            booked_flights_info.append(flight)  # Menambahkan informasi penerbangan yang telah dipesan
                            print(f"\nInformasi Penerbangan:\nNomor Penerbangan: {flight.flight_number}\nTujuan: {flight.destination}\nWaktu Keberangkatan: {flight.departure_time}\nHarga Tiket: {flight.price}\nTotal Penjualan Tiket: {flight.total_sales}")
                            break
                        else:
                            print(f"Maaf, penerbangan yang dipesan telah penuh.")
                            print(f"Sisa kursi untuk Penerbangan {flight.flight_number} ke {flight.destination}: {flight.available_seats}")
                            break
                else:
                    print("Nomor penerbangan tidak valid.")
                    continue
                break
        elif choice == "3":
            if booked_flights_info:
                print("\n--== Pesanan Anda ==--")
                print("Jika ada yang memiliki 2 atau lebih pesanan yang sama (duplikat), Harganya kita totalkan semua jika memesan 2 atau lebih di pesawat yang sama")
                for flight_info in booked_flights_info:
                    print(f"\nInformasi Penerbangan:\nNomor Penerbangan: {flight_info.flight_number}\nTujuan: {flight_info.destination}\nWaktu Keberangkatan: {flight_info.departure_time}\nHarga Tiket: {flight_info.price}\nTotal Penjualan Tiket: {flight_info.total_sales}")
            else:
                print("\nAnda belum memesan tiket pesawat apapun.")
        elif choice == "4":
            if booked_flights_info:
                print("\n--== Pesanan Anda ==--")
                print("Jika ada yang memiliki 2 atau lebih pesanan yang sama (duplikat), Harganya kita totalkan semua jika memesan 2 atau lebih di pesawat yang sama, sehingga harga total pesanan yang terduplikat tersebut sama harganya")
                for flight_info in booked_flights_info:
                    print(f"\nInformasi Penerbangan:\nNomor Penerbangan: {flight_info.flight_number}\nTujuan: {flight_info.destination}\nWaktu Keberangkatan: {flight_info.departure_time}\nHarga Tiket: {flight_info.price}\nTotal Penjualan Tiket: {flight_info.total_sales}")
            print("\nTerima kasih telah menggunakan layanan kami.")
            if booked_flights_info:
                print("Semoga selamat dalam penerbanganmu sampai tujuan")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

# Main Program
main()

