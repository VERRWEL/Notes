
#Varel Wungow 32230062
"""
Algoritma Keseluruhan Program  :
1. user memberi setidaknya satu atau lebih inputan dalam bentuk integer
yang merepresentasikan Arrival Time dan Burst Time dari setiap proses.
2. setiap inputan akan dimasukkan ke dalam sebuah list secara berurut.
dan akan merepresentasikan P1, P2, P3, dan seterusnya secara berurut.
3. algoritma SJF akan berjalan dan akhirnya mengoutput procses, arivaltime,
dan Burst Time, beserta perhitungan Average Time.
"""

# list untuk menampung arrival time dan burst time
list_AT_proses = []
list_BT_proses = []

# loop inputan arrival time dan burst time dari setiap proses
exit = False
while exit == False:
    input_AT = int(input("Masukkan Arrival Time: "))
    input_BT = int(input("Masukkan Burst Time: "))
    list_AT_proses.append(input_AT) # appending arival time ke list
    list_BT_proses.append(input_BT) # appending burst time ke list
    exit = input("Apakah ingin melanjutkan? (Y/N) ")
    if exit == "N" or exit == "n":
        exit = True
    elif exit == "Y" or exit == "y":
        exit = False

# algoritma SJF
"""
Algoritma SJF :
1. cek waktu sekarang berapa
2. cek proses apa saja yang siap dieksekusi relatif dengan waktu sekarang
3. jika hanya ada satu proses yang siap, maka eksekusi proses tersebut.
tapi jika ada lebih dari satu proses yang siap, maka eksekusi proses yang
memiliki BT terrendah.
4. setelah proses itu selesai, kasi status "selesai" agar proses tidak mengulang
secara tidak sengaja.
"""

time = 0
AT_process_in_range = []
BT_process_in_range = []
def SJF(time):
    for process_AT in list_AT_proses:
        if process_AT <= time:
            AT_process_in_range.append(process_AT)

SJF(time)

# output proses, arrival time, dan burst time. dan hasil perhitungan average time
print ("Proses\tAT\tBT")
for i in range(len(list_AT_proses)):
    print ("  P"+str(i+1)+"\t"+str(list_AT_proses[i])+"\t"+str(list_BT_proses[i]))
