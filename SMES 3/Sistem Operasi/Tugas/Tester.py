
#SJF

def recursive(time, arrived_proc, process): 

    if time >= cap:
        print("\nFINNISHED")
        print("LAST TICK", time)
        print()
        return arrived_proc
    
    # loop untuk mengecek proses yang sudah diterima
    for process_AT in process:
        if process[process_AT][0] <= time:
            arrived_proc[process_AT] = process[process_AT]
 
    # print waktu sekarang dan proses yang diterima
    print("tick", time)
    print("\tarrived:", list(arrived_proc.keys()))
    
    # cek jika hanya ada satu proses yang tersedia, maka eksekusilah itu
    if len(arrived_proc) == 1:
        time = time + arrived_proc[list(arrived_proc.keys())[0]][1]
        print("\tEXECUTING", list(arrived_proc.keys())[0], "for being the only ready process")

        process.pop(list(arrived_proc.keys())[0])
        arrived_proc.pop(list(arrived_proc.keys())[0])

        recursive(time, arrived_proc, process)
        return
    
    # cek jika ada lebih dari satu proses yang tersedia maka eksekusilah yang memiliki BT terpendek
    elif len(arrived_proc) > 1:
        now = list(arrived_proc.keys())[0]
        for temp in list(arrived_proc.keys()):
            if arrived_proc[temp][1] < arrived_proc[now][1]:
                now = temp

        print("\tEXECUTING", now, "for having lowest BT")
        time = time + arrived_proc[now][1]
        process.pop(now)
        arrived_proc.pop(now)

        recursive(time, arrived_proc, process)
        return
    
    # cek jika tidak ada proses yang belum sampai
    else:
        time = time + 1
        recursive(time, arrived_proc, process)
        return

process = {
    'P1' : [0,7],
    'P2' : [2,4],
    'P3' : [4,1],
    'P4' : [5,4]
}

tmp_cap = []
for cap_BT in list(process.keys()):
    tmp_cap.append(process[cap_BT][1])
cap = sum(tmp_cap)


arrived_proc = {}
finished_proc = {}
time = 0
recursive(time, arrived_proc,process)