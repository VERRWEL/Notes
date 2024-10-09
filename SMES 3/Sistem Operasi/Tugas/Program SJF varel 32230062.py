
#non-preemtive SJF
def rekursif_sjf(time, arrived_proc, process): 

    if time >= cap:
        print("\nFINNISHED PADA WAKTU", time)
        return arrived_proc
    
    # loop untuk mengecek proses yang sudah diterima
    for process_AT in process:
        if process[process_AT][0] <= time:
            arrived_proc[process_AT] = process[process_AT]
 
    # print waktu sekarang dan proses yang diterima
    print("waktu", time, "ready:", list(arrived_proc.keys()))
    
    # cek jika hanya ada satu proses yang tersedia, maka eksekusilah itu
    if len(arrived_proc) == 1:
        
        print("\tEXECUTING", list(arrived_proc.keys())[0], "karena satu-satunya proses yang ready")

        # calculating waiting time for the executed process
        temp_calc_waiting = arrived_proc[list(arrived_proc.keys())[0]][0] - time
        print(f"\t{list(arrived_proc.keys())[0]} waiting time: {abs(temp_calc_waiting)}\n")
        finished_proceses_waiting_time.append(abs(temp_calc_waiting))

        time = time + arrived_proc[list(arrived_proc.keys())[0]][1]
        process.pop(list(arrived_proc.keys())[0])
        arrived_proc.pop(list(arrived_proc.keys())[0])

        rekursif_sjf(time, arrived_proc, process)
        return
    
    # cek jika ada lebih dari satu proses yang tersedia maka eksekusilah yang memiliki BT terpendek
    elif len(arrived_proc) > 1:
        now = list(arrived_proc.keys())[0]
        for temp in list(arrived_proc.keys()):
            if arrived_proc[temp][1] < arrived_proc[now][1]:
                now = temp

        print("\tEXECUTING", now, "karena memiliki BT terrendah")

        # calculating waiting time for the executed process
        temp_calc_waiting = arrived_proc[now][0] - time
        print(f"\t{now} waiting time: {abs(temp_calc_waiting)}\n")
        finished_proceses_waiting_time.append(abs(temp_calc_waiting))

        time = time + arrived_proc[now][1]
        
        process.pop(now)
        arrived_proc.pop(now)

        rekursif_sjf(time, arrived_proc, process)
        return
    
    # cek jika tidak ada proses yang belum sampai
    else:
        time = time + 1
        rekursif_sjf(time, arrived_proc, process)
        return

# fungsi rekursif input proses
def rekursif_input_proses(Pid, process, maxim): 
    if Pid > int(maxim):
        return

    try:
        AT =input(f"masukkan arrival time P{Pid} ")
    except:
        print("input error, tolong masukkan angka saja")
        rekursif_input_proses(Pid, process, maxim)
        return
    try: 
        BT = input(f"masukkan burst time P{Pid} ")
    except:
        print("input error, tolong masukkan angka saja ")
        rekursif_input_proses(Pid, process, maxim)
        return
    
    prosesID= f"P{Pid}"
    process[prosesID] = [int(AT), int(BT)]
    Pid = Pid + 1
    rekursif_input_proses(Pid, process, maxim)

# dictionary yang menampung masing-masing proses di key dictionary, arrival time dan burst time di value dictionary
process = {}

Pid = 1
maxim = input("berapa proses yang ingin dieksekusi? ")
rekursif_input_proses(Pid, process, maxim)

# print proses
print()
for process_AT in process:
    print("proses", process_AT, "AT:", process[process_AT][0], "BT:", process[process_AT][1])

tmp_cap = []
for cap_BT in list(process.keys()):
    tmp_cap.append(process[cap_BT][1])
cap = sum(tmp_cap)

arrived_proc = {}
finished_proceses_waiting_time = []
time = 0
print()
rekursif_sjf(time, arrived_proc,process)

# print hasil
print("waiting time dari masing masing proses :", finished_proceses_waiting_time)
print("average waiting time = ", sum(finished_proceses_waiting_time)/len(finished_proceses_waiting_time))