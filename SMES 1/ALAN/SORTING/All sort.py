#making a random array
import random
data = []
for i in range(0,5):
    x = random.randint(1,100)
    data.append(x)
print("RANDOMIZED UNSORTED DATA :\n",data)

def selection_sort(arr):
  #selection sort
  print("\nSELECTION SORT")
  for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  print("SORTED DATA :\n",arr)

def buble_sort(arr):
    #buble sort
    print("\nBUBLE SORT")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("SORTED DATA :\n",arr)

def insertion_sort(arr):
  #buble sort
  print("\nINSERTION SORT")
  for i in range(1, len(arr)):
    current_element = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > current_element:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = current_element

  print("SORTED DATA :\n",arr)

selection_sort(data)
buble_sort(data)
insertion_sort(data)