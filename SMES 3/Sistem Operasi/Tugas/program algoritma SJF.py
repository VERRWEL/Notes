class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0

def psjf_scheduler(processes):
    # Mengurutkan proses berdasarkan waktu kedatangan
    processes.sort(key=lambda x: x.arrival_time)
    
    current_time = 0
    completed = 0
    total_waiting_time = 0
    timeline = []
    
    while completed < len(processes):
        # Mencari proses yang sudah tiba dan memiliki sisa waktu burst terpendek
        eligible = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
        if not eligible:
            current_time += 1
            continue
        
        shortest = min(eligible, key=lambda x: x.remaining_time)
        
        # Jika proses baru dimulai, catat waktu mulainya
        if shortest.remaining_time == shortest.burst_time:
            shortest.start_time = current_time
        
        shortest.remaining_time -= 1
        current_time += 1
        
        timeline.append(shortest.pid)
        
        # Jika proses selesai
        if shortest.remaining_time == 0:
            completed += 1
            shortest.completion_time = current_time
            shortest.waiting_time = shortest.completion_time - shortest.arrival_time - shortest.burst_time
            total_waiting_time += shortest.waiting_time
    
    avg_waiting_time = total_waiting_time / len(processes)
    return timeline, avg_waiting_time

# Contoh penggunaan
if __name__ == "__main__":
    processes = [
        Process(1, 0, 7),
        Process(2, 2, 4),
        Process(3, 4, 1),
        Process(4, 5, 4)
    ]
    
    timeline, avg_waiting_time = psjf_scheduler(processes)
    
    print("Timeline eksekusi:", " ".join(map(str, timeline)))
    print(f"Rata-rata waktu tunggu: {avg_waiting_time:.2f}")
    
    print("\nDetail setiap proses:")
    for p in processes:
        print(f"Proses {p.pid}: Waktu Mulai = {p.start_time}, Waktu Selesai = {p.completion_time}, Waktu Tunggu = {p.waiting_time}")