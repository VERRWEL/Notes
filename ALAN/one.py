# BINARY SEARCH
import random

arr = []

while True:
    ran = random.randint(1,9)
    if ran not in arr:
        arr.append(ran)
    if len(arr) == 10:
        break
    
print(arr)