n, t = None, None
while n is None or t is None:
    input_str = input("masukan potongan pizza ke berapa dan banyaknya potongan: ")
    try:
        n,t = map(int, input_str.split())
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
        
pizza = [0] * (n + 1)

for i in range(1,n + 1):
    orang_pertama = set(map(int, input("masukan banyak potongan dimakan: ").split()))
    slices_liked1 = set(map(int, input(f"potongan favorite orang pertama: ").split()))

orang_kedua = int(input("masukan banyak potongan yang dimakan orang kedua : "))
slices_liked2 = set(map(int, input(f"potongan favorite orang kedua: ").split()))

for me in orang_pertama:
    while me <= n and pizza[me] > 0:
        print(f"Slice #{me} is eaten by Aku")
        pizza[me] -= 1
        
for me in slices_liked2:
    while me <= n and pizza[me] > 0:
        print(f"{slices_liked2} akan dimakan oleh orang kedua")
        pizza[me] -= 1

if t <= n:
    print(f"Sisa potongan akan dimakan orang ketiga")
    pizza[t] -= 1


total_slices_eaten = t

if total_slices_eaten == 0:
    print("Only one slice was eaten in total.")
else:
    print(f"Aku makan {orang_pertama} slices.")
    print(f"orang kedua makan {orang_kedua} slices.")
    print(f"orang ketiga {total_slices_eaten - len(orang_pertama) - orang_kedua - 1} slice.")
    print("End of simulation")