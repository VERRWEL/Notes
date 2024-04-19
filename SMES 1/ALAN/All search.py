data = [5,12,20,21,25,33,50]
search = int(input("berapa value index yang ingin dicari? "))

def linear_search(arr, cari):
    for i in range(len(arr)):
        if arr[i] == cari:
            print("elemen ditemukan di index", i)
            break
        if i == len(arr) - 1:
            print("elemen tidak ditemukan")
        
def binary_search(arr, cari):
    low = 0
    high = len(data) - 1
    while(low <= high):
        mid = int((low+high) / 2)
        if arr[mid] == cari:
            print("elemen ditemukan di index", mid)
            break
        elif data[mid] < cari:
            low = mid + 1
        else:
            high = mid - 1
    if low > high:
        print("elemen tidak ditemukan")
    
def interpolation_search(arr, cari):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = int(low +(((cari-arr[low])*(high-low)) / (arr[high]-arr[low])))
        if (cari == data[mid]):
            print("elemen ditemukan di index", mid)
            break
        elif cari < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if low > high:
        print("elemen tidak ditemukan")
        
linear_search(data, search)
binary_search(data, search)
interpolation_search(data, search)